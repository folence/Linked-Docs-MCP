---
title: Multiplayer - Factorio Wiki
source: https://wiki.factorio.com/Multiplayer
scraped_at: 2025-10-21 14:29:16
tags: [web, documentation]
---

# Multiplayer - Factorio Wiki

**Source:** [https://wiki.factorio.com/Multiplayer](https://wiki.factorio.com/Multiplayer)

In addition to being a single-player game, Factorio also supports multiplayer, allowing many players to cooperate and assist each other, or work against each other in pvp. This page documents how to set up a multiplayer game, how to join one, and the Multiplayer Admin features for managing other users and the server. By default, multiplayer games run the CO-OP freeplay scenario where all players work together to launch a rocket with a satellite into space. Other scenarios, including PvP maps, are available for download from the Maps and Scenarios forum .

## Contents

- 1 Setting Up a Multiplayer Game 1.1 Dedicated/Headless server 1.2 Setting up a Linux Factorio server 1.2.1 Basic installation 1.3 How to list a server-hosted game on the matching server 1.4 Technical Implementation Details 1.5 DNS SRV Records 1.6 Miscellaneous Tips
- 2 Joining a Multiplayer game 2.1 Joining by IP 2.2 Joining via server list 2.3 Joining through Steam 2.4 Joining a local LAN game 2.5 Connecting to a Server Behind NAT
- 3 PvP 3.1 Forces
- 4 History 4.1 Narrative history 4.2 Version history

## Setting Up a Multiplayer Game

Multiplayer games can be joined, hosted while playing, or hosted by a dedicated server.  Multiplayer games can be advertised to other players on the same LAN or worldwide.

To start playing a multiplayer game, select the Multiplayer button from the main menu. Then, choose one of these options to host and play:

- Host new game : Specify the desired scenario, adjust the map generator settings, and set the server visibility. The server visibility determines how your game will be advertised to other players. You can choose from: Public : Your game will be listed on the public games list. Steam : Enables or disables the "Join Game" feature through Steam. LAN : Your game will be listed on your local network.
- Host saved game : Pick a saved game from the list and set the server visibility as above.

To join an existing game, choose one of these options:

- Browse public games : Search for and join any public game that meets your criteria.
- Browse LAN games : Join any game that is hosted on your local network.
- Connect to address : Join any game by entering the server’s IP address. This option is useful if the host does not use any server visibility.

Notes and tips:

- All game instances need the installation of exactly the same game-versions and mods.
- Factorio servers use port 34197 . The port can be changed in the config file.
- Factorio uses UDP only . The game builds its own "reliable delivery" layer built on UDP to deal with packet loss and reordering issues. Make sure you configure your router's port forwarding correctly for port 34197 . Make sure your router does not randomize the source port on packets outbound from 34197 .  Some routers do this and require additional configuration to prevent it. Make sure there is no firewall or anti-virus blocking the UDP-packets.
- The hard limit for the number of players is 65,535 . However, practical limit for this is much lower, popular streamers have managed to get well over a hundred players.

### Dedicated/Headless server

A dedicated (or headless) server can be started using the --start-server command line option. You can run factorio --help to get a list of all command-line arguments that Factorio accepts. Any version of the game can be run in headless mode, though for Linux servers it may be preferable to use the Headless version of the game, which does not include graphics to reduce download size. This can be found on the factorio.com Downloads page .

In the headless mode:

- Graphics are not initialized (faster start up, less memory usage, works on completely headless servers)
- Game starts immediately and loads a save given as a parameter to the command
- The server has no character in game
- Game is paused while there are no players connected (though this can be overridden using the no-auto-pause option in the server-settings.json)
- Saves the game on exit (and autosaves normally)

0.13 onwards expects --start-server to be followed by a path to a save file.

You will need to create your save file before you start the server, as the dedicated server REQUIRES a save file to be provided. This can easily be done using the --create command-line argument. For example:

```
./bin/x64/factorio --create ./saves/my-save.zip       # This creates a new save, as if by clicking the New Game button in the GUI
```

```
./bin/x64/factorio --start-server ./saves/my-save.zip # This starts a server that will host the file created on the previous line
```

There are several JSON configuration files that factorio can make use of to change the server and map settings:

- map-gen-settings to set parameters used by the map generator such as width and height, ore patch frequency and size, etc.
- map-settings to control pollution spread, biter expansion and evolution , and more
- server-settings which consolidated several command-line options into a single file

Example files for each of these parameters are included in the data subdirectory, and are also visible on Wube's github here: https://github.com/wube/factorio-data

The --map-gen-settings and --map-settings options must be used with the --create option when you create a new map.  For example:

```
./bin/x64/factorio --create saves/my-save.zip --map-gen-settings my-map-gen-settings.json --map-settings my-map-settings.json
```

Starting the factorio server requires you to specify the location of the server-settings.json file. By default this is in the factorio data folder. For example to start factorio using the most recent saved map, you would run:

```
./bin/x64/factorio --start-server-load-latest --server-settings ./data/server-settings.json
```

On windows, it may be useful to start the server with a .bat file. The bat file should have the following content:

```
start /wait .\bin\x64\factorio.exe --start-server-load-latest --server-settings .\data\server-settings.json
```

See Command line parameters for more command line parameters.

### Setting up a Linux Factorio server

Note: Factorio now requires glibc version 2.31, but CentOS/RHEL 7 only ship with version 2.17 so this guide will no longer work without manually compiling glibc 2.31 .

This step-by-step guide has been verified on fresh CentOS 7 and RHEL 7 installs but should be applicable with little to no changes on most distributions.

The guide assumes you will install the headless server under /opt/factorio , adjust paths according to your own setup. We will also suggest that you run the Factorio server as a separate user to harden security of your setup.

Note that there are two distinct packages for Linux that can be used to run a headless server. First is the usual Linux download, that contains the full game. The other is the special headless package . The headless package does not contain any files irrelevant for a pure server, such as graphics and sounds. It is also not linked against libraries that may not be present on a server machine, such as Xlib, libGL or libasound. This option should be selected if running in a 3rd party hosted server.

This guide does not handle firewall/port forwarding since this can be done in various ways on Linux (make sure to read up how this is done as a Linux admin on your particular distribution)

#### Basic installation

- Download the selected package -- either full game or the headless package -- and upload the Linux tar.gz or tar.xz package to your server /tmp
- Extract the package in /tmp to /opt/factorio

```
$cd /opt/

$sudo tar -xzf /tmp/factorio.tar.gz # Use the correct file name. It includes the factorio version number
$sudo tar -xJf /tmp/factorio.tar.xz # if you downloaded a .tar.xz file (ver 0.15.x)
```

- Add a new user to your system and assign ownership of the factorio dir to it (please, do not run as the root user, sudo may be needed)

```
$useradd factorio
$chown -R factorio:factorio /opt/factorio
```

- Try the binary

```
$su factorio
$/opt/factorio/bin/x64/factorio --start-server savename
```

As long as it fails saying it cannot find/open the savename.zip you are set! Just upload a save from your own computer and put it in the /opt/factorio/saves directory, or use the --create ./saves/newgame.zip argument.

### How to list a server-hosted game on the matching server

In order to publish the game to the matching server, Factorio needs to be given some more information than just the save file location. These information are provided in a server settings file .

To create a server settings file, look at the example file located in data/server-settings.example.json in the Factorio Application directory . The recommended way is to make a copy of this example file and edit the copy.

The following values can be changed:

- Visibility for server browser: May be either public, LAN or hidden. Public: The server will appear in the public server list. This requires the login credentials below to be filled in. LAN: The server will not appear in the public server list, but will be available through the Play On LAN button Hidden: Clients will have to connect using the server's IP address
- User credentials using a username and password or authentication token (found on the factorio website or in the player-data.json): These are necessary if you wish to make the server public. Otherwise, they can be left empty. For security reasons it is recommended to use authentication token as this document is stored as plain text. Though it should be noted that an authentication token is a sensitive piece of information as well, and you are well-advised to keep it secret.
- Server Password Field name is game_password
- Whether to verify user identity

(There are additional values in v0.14 of factorio.)

### Technical Implementation Details

Notes about some technical details surrounding multiplayer have been published by the development team in several Friday Facts blog posts:

- Lock step architecture
- Client-server connections
- NAT punching, introduced in 0.13

### DNS SRV Records

Factorio supports DNS SRV records since 1.1.67.

This makes it easier to have multiple Factorio servers on a single host and allow users to connect to them with distinct subdomains instead of having to enter port numbers.

The service name is _factorio and it only supports _udp protocol.

Example:

```
Domain: subdomain.domain.tld
IP:     192.0.2.2
Port:   10002

DNS records:
subdomain.domain.tld     IN A   192.0.2.2 
_factorio._udp.subomain.domain.tld IN SRV 0 0 10002 subomain.domain.tld.
```

Now a Factorio client connecting to subdomain.domain.tld will actually connect to subdomain.domain.tld:10002

Example screenshot of config in Cloud Flare:

Log Entries:

- Factorio will log a "DNS SRV lookup returned [...]" message when it found a SRV record for the given domain
- With verbose logging Factorio will also log "DNS SRV lookup for [domain] didn't return any usable records" when there's no SRV record

### Miscellaneous Tips

- The key for console commands is also used initiate chat in multiplayer. To execute a command instead of chatting, you need to type /c before the command. Commands executed are visible to all players . Additionally, the multiplayer game must have been started with commands allowable for commands to work.
- Set the player's color using the command

```
/color r g b
```

r, g and b are for red, green and blue respectively (possible values are between 0 and 1, use this site to convert colors to rgb numbers).

- To give yourself admin access, you need to create a server-adminlist.json in the same directory as factorio-current.log. The file should contain a list of admins, like so: [ "user1", "user2" ]

This file will be created if you promote a player through the console.

## Joining a Multiplayer game

As of version 0.13, players no longer necessarily have to port-forward to play with others. Players may join each other through Steam, or by just the port-forwarded host.

Players wishing to join a game may do so in multiple ways:

- Joining by directly inputting a public IP and port into Factorio.
- Selecting the server from the active public server menu.
- Joining through Steam's services.
- Playing a local LAN game.

### Joining by IP

To join a multiplayer game by IP, you will need to know the public IP of a valid server. You can find this through social media, websites, or by word of mouth. After acquiring the IP and port, simply go to play -> Multiplayer -> Connect to server, and provide all the information it asks for.

If the server has been set up correctly to accept public connections, you should be able to join the game.

### Joining via server list

Factorio's devs keep a list of all public servers that declare themselves to the service, allowing players to join directly through Factorio. Most of these servers will be password-requiring, but many completely public servers can be connected to. To join via server list, go to Play -> Multiplayer -> Browse public games. Provide your Factorio.com login if asked, and a list of public servers will appear. Simply select one.

### Joining through Steam

Steam provides a "game invite" system, simply use that to join. You can find more info about how to use steam in it's documentation. This is the most recommended way for the average player to use multiplayer with their friends, as it allows Steam to handle everything .

### Joining a local LAN game

If you have some friends on the same internet connection as you (in the same building or network), you may play a LAN game. Simply go to Play -> Multiplayer -> Play on LAN.

### Connecting to a Server Behind NAT

Factorio requires that the server (in client-server mode) have a publicly accessible IP address or that all players are on the same LAN. If you are behind NAT, you must set up port forwarding ( see above for port number) or use virtual LAN software such as Hamachi.

Multiplayer games will be launched in client-server mode (also multiplayer forwarding mode). In this mode, all clients send their network traffic to the server and the server forwards the traffic to the other clients. The advantage of this is that it allows games where some players are inside a LAN and others are outside. The disadvantage may be slightly more lag as packets must travel an extra hop (through the server).

- Forwarding ports without logging into your router
- A guide for connecting with Hamachi

## PvP

In PvP mode, players can be on different forces. Each force can have one (free-for-all) or more players (teams). Each force has its own independent research progression. Additionally, each force's Military units and structures will attack other players as enemies, unless a cease fire is set. Note that, depending on the scenario, cease fires may be unidirectional — setting a cease fire with an opposing force does not guarantee a cease fire from them in return.

To start a PvP game, you can select the 'PvP' scenario from the 'Play' menu, or download a custom scenario which also supports PvP.

After downloading a PvP scenario, you need to move it to your application directory, and create the multiplayer game using the scenario.

- Download the scenario and place the scenario directory in the scenarios directory within your user data directory .
- Launch Factorio
- Click Play
- Click Multiplayer
- Click Scenario
- Choose the PvP scenario you want and click Create
- Choose latency and other settings, then click Play
- Other players can now join the game

### Forces

Forces can be manually created via the console. This allows any map/scenario to be used for PvP. This may not be as convenient as a pre-made PvP scenario, as there will be no way for players to turn on/off cease fires other than through the console.

Each created force has its own research progression and different forces may attack each other.

The console commands for setting up and controlling forces are below:

```
game.create_force("Name")
--Creates the force "Name"

game.players["Player_name"].force = game.forces["Name"]
--Sets this player to the new force

game.forces["Name"].set_cease_fire("Other_force_name", true)
--Sets the new force ceasefire to the "other force"

game.forces["Name"].set_spawn_position({x = 10, y = 20}, game.surfaces[1])
--Sets the spawn position of the force

game.print(#game.forces)
--Prints the number of forces

for name, force in pairs (game.forces) do
   game.print(name)
end
--Prints the name of all the forces
```

The ability of players and entities belonging to one force to interact with structures belonging to another, non-friendly force is limited. However, some types of interactions are still possible:

## History

### Narrative history

Because of the potentially immense amount of activity on a map, the game engine utilizes a lock step architecture . All instances of the game run full simulations of the entire world and only player actions are transferred across the network.

Multiplayer games were introduced to Factorio with version 0.11.0. The only connection method available was peer-to-peer mode which meant every player had to be able to directly communicate with every other player. In version 0.12.4, a client-server mode of communication was introduced in which the server (either a dedicated one or the player who hosted the game) relays messages to all peers. This means that direct connection between all players is no longer necessary. As of version 0.13, P2P connecting is completely removed.

As of version 0.12.0, the game features "latency hiding" mechanics where the game simulates some of the player's actions locally to make some common interactions (such as moving the player's character) more fluid.  Not every action is a part of latency hiding – most notably, car or train driving and shooting are not a part of it.

### Version history

Maintainer note: The following history may not be fully up to date, or comprehensive. Factorio's multiplayer has undergone a great deal of small changes since its inception, however this history will provide a rough overview.

- 0.14.14 : Added multiplayer server option "Autosave only on server". Deconstructing/canceling deconstruction sets the "last user" on an entity. Decreased the size of connection accept message with lot of mod which could help some people with 50+ mod multiplayer games.

- 0.14.13 : Reconnecting to multiplayer game that the player is already in (due to being dropped, most often) instantly closes the previous connection and connects the player.

- 0.14.11 : Multiplayer user names can only consist of letters, and -_. characters.

- 0.14.10 : Disabled 32bit (x86) multiplayer. All hosts and members must be running the 64bit (x86_64) version of the game.

- 0.14.8 : More than 10 players in one game will reduce the rate the game is saved to the server.

- 0.14.6 : Username is now set to username setting, not email.

- 0.14.5 : Added AFK Auto kick interval to multiplayer host settings (with never as default).

- 0.14.3 : When save of scenario is loaded in multiplayer, it's scenario is saved in user scenarios. Added /time command to print the current map age. Added option to host multiplayer game with scenario (it only had new game/load game there).

- 0.14.2 : Can specify limit of upload speed when hosting.

- 0.14.0 : Server doesn't stop/slow down the game when some client is too slow, stops communicating or saves the game longer than the server. Players automatically quit game after 3 desyncs. Removed the option to enable/disable latency hiding, it is always on on clients (and off on the server).

- 0.13.10 : Server stdout messages now contain time stamps and message-type tags

- 0.13.2 : Limit multiplayer player name to 60 characters.

- 0.13.0 : Improved Multiplayer game UX Server games are published to the server and clients can browse existing games. Removed multiplayer peer-to-peer mode. Building sound is played also for other players in multiplayer.

- 0.12.31 : Human readable error notice when multiplayer connection wasn't successful. ( https://forums.factorio.com/23132 ) Improved map download speed when connecting to multiplayer game.

- 0.12.30 : Mod checksums are calculated when the game starts and are compared with other peers when joining a multiplayer game. This is to ensure everyone has exactly the same mod in order to prevent desyncs caused by local changes made to mod files.

- 0.12.28 : Added --port to specify which network port the game should use, when hosting with --start-server or --mp-load-game.

- 0.12.27 : The report of different mods when trying to connect to multiplayer game is now scroll-able when needed. Better message when the server leaves a multiplayer game

- 0.12.11 : Added --no-auto-pause: When running as a server, --no-auto-pause will prevent stopping the game when no players are connected.

- 0.12.9 : Added resume button to multiplayer game menu

- 0.12.7 : New command line options for the headless server: --disallow-commands and --peer-to-peer

- 0.12.5 : Multiplayer broadcast (heartbeats) is done via a single message when not using peer2peer. Further optimizations in size of the Multiplayer heartbeat (message sent every tick). LatencyState is suspended when player is killed (and waiting for respawn) in Multiplayer.

- 0.12.4 : Simple mechanism for multiplayer relaying via the server. Less annoying glitches when running and shooting in multiplayer with latency hiding.

- 0.12.0 : Multiplayer latency hiding (gives impression that some common tasks are performed immediately) Factorio can run as a dedicated server without graphics. Basic PvP: New forces can now be created and merged back together; a cease-fire can be agreed upon between forces IPv6 support for multiplayer. DNS names can be used when connecting to multiplayer game. Player's logistic filters are now remembered after respawn in multiplayer Smaller multiplayer heartbeat packet size.

- 0.11.19 : Multiplayer dropping threshold is doubled during map upload / download.

- 0.11.17 : Autosaves in multiplayer are performed at the same time by all clients (interval is set by hosting player). Progress bar is shown when non-responsive peers are about to be dropped from the game in the Multiplayer. Progress bar is shown when other peers in multiplayer are saving map.

- 0.11.16 : Revived character (after dying in multiplayer) are placed on the spawn point instead of the center of the map.

- 0.11.2 : Mods that don't affect game state are not needed to be synchronized when playing multiplayer game or replaying game.

- 0.11.0 : Introduced

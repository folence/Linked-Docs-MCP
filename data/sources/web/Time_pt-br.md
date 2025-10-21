---
title: Tempo - Factorio Wiki
source: https://wiki.factorio.com/Time/pt-br
scraped_at: 2025-10-21 15:48:01
tags: [web, documentation]
---

# Tempo - Factorio Wiki

**Source:** [https://wiki.factorio.com/Time/pt-br](https://wiki.factorio.com/Time/pt-br)

O conceito do termo Tempo em Factorio é usado em vários sentidos e implementações, principalmente na fabricação de itens e no tempo do jogo.

## Tempo e velocidade de fabricação

Ao passar o mouse sobre a receita de um item, o jogador pode ver um símbolo de relógio e um número. Esta é a quantidade de tempo necessária para criar o item em segundos na velocidade de criação 1. O jogador sempre trabalha na velocidade 1, já as máquinas de montagem têm diferentes tempos de fabricação. Os módulos também afetam o tempo de fabricação, acelerando ou desacelerando para algum outro benefício. O jogador , ao fazer itens com a mão , tem um multiplicador de tempo de 1, então itens que levam 10 segundos para serem fabricados levarão 10 segundos, mas uma máquina de montagem 1 tem um multiplicador de tempo de 0.5 então, dessa maneira levará 20 segundos. É importante levar isso em consideração ao criar configurações com proporções adequadas.

## Ticks

Essa é a unidade básica dentro do Factorio. Se o jogo está na velocidade 1, terá 60 ticks em cada segundo em tempo real, levando a 60 atualizações por segundo, ou seja um UPS curto. Isso significa que 1 tick deve sempre levar 1/60 de segundo em tempo real (0.01667 segundos). No entanto, é possível alterar a velocidade do jogo em [1] usando mods ou comandos de console, portanto, é possível que os ticks não levem 0,01667 segundos em tempo real. Além disso, a velocidade do jogo diminuirá automaticamente quando o computador que está executando o jogo não puder fazer todos os cálculos necessários nos 0,01667 segundos desejados em tempo real. O "show-fps" da opção de debug permite ver o UPS atual, que pode ser usado para estimar quanto tempo um tick leva atualmente.

## Segundos

Como mencionado acima, sempre deve haver 60 ticks a cada segundo; portanto, 1 segundo no jogo é igual a 60 ticks no jogo. A proporção de 60 para 1 também é aplicada quando a velocidade é menor, portanto, um segundo no jogo pode demorar mais que um segundo em tempo real.

## Dias

Um dia no jogo dura 25000 ticks ou 416,66 ~ segundos no jogo.

A luz varia ao longo do dia em um ciclo composto por 4 fases:

| Fase | Nome internal | Comportamento | Hora do dia no início | Hora do dia no final | Duração (em ticks ) | Duração (em segundos) |
| Dia | dawn | totalmente claro | 0.75 | 0.25 | 12500 | 208.33~ |
| pôr do sol | dusk | escurecimento | 0.25 | 0.45 | 5000 | 83.33~ |
| noite | evening | totalmente escuro | 0.45 | 0.55 | 2500 | 41.66~ |
| nascer do sol | morning | clareamento | 0.55 | 0.75 | 5000 | 83.33~ |

```
------------- dia ---- --><--- pôr do sol---->< noite -><-- nascer do sol--><-------- dia -----------
  
% 0    5    10   15   20   25   30   35   40   45   50   55   60   65   70   75   80   85   90   95  100
  |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
```

Durante o pôr do sol, o nível de luz diminui linearmente de totalmente claro para totalmente escuro. Durante o nascer do sol, aumenta linearmente do escuro para a luz. Essa inclinação linear não se aplica necessariamente aos valores retornados por LuaSurface.darkness . Durante a noite o jogador vai ligar sua lanterna que está no seu capacete (ou faróis caso esteja em um veículo ), já uma lâmpada só acenderá caso tenha eletricidade.

Nota: O tempo real entre as fases pode variar +/- uma marca devido a erros de curvas.

set terminal pngcairo size 1200,800 enhanced font 'Arial,14'
set output 'exp3.png'

set title 'Floyd-Warshall vs Dijkstra: Inflection Points' font ',18'
set xlabel 'Graph size N (nodes)' font ',14' 
set ylabel 'Break-even queries Q*= T_FW / T_D' font ',12'

set grid back lc rgb '#dddddd' lw 1

# Style points and lines
set pointintervalbox 3
set style line 1 lc rgb 'red' lt 1 lw 3 pt 7 ps 2
set style line 2 lc rgb 'red' lt 1 lw 2 pt 7 ps 1.5

plot 'exp3.dat' using 1:4 w lp ls 1 title 'Q* (queries after FW wins)'

replot

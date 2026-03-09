# exp1.gp
# gnuplot script to compare Floyd-Warshall vs Djistrika
# Using linear scales instead of log-log plot from our presentation


set datafile separator whitespace
set key top left
set grid

# save as PNG images
set terminal pngcairo size 1200,800 enhanced font 'Arial,12'

# execution time comparison
set title "Execution Time: Floyd-Warshall vs Djistrika"
set xlabel "Number of Vertices (n)"
set ylabel "Execution Time (seconds)"
unset logscale
set format y "%g s"

plot 'expirement_1.dat' using 1:2 title "Floyd-Warshall" with linespoints lt 1 lw 2 pt 7 lc rgb "red", \
     '' using 1:4 title "Djistrika (all-pairs)" with linespoints lt 3 lw 2 pt 5 lc rgb "blue"

pause -1

# Time complexity plot
set output 'time_complexity.png'
replot

# memory usage comparison
set title "Memory Usage: Floyd-Warshall vs Djistrika"
set xlabel "Number of Vertices (n)"
set ylabel "Memory Usage (MB)"
unset logscale
set format y "%g MB"

plot 'expirement_1.dat' using 1:3 title "Floyd-Warshall" with linespoints lt 2 lw 2 pt 7 lc rgb "red", \
     '' using 1:5 title "Djistrika" with linespoints lt 4 lw 2 pt 5 lc rgb "blue"

pause -1


# Memory complexity plot
set format y "%g MB"
set output 'memory_usage_visual.png'
set title "Memory Complexity (Linear Scale)"
set xlabel "Number of Vertices (n)"
set ylabel "Memory Usage (MB)"
plot 'expirement_1.dat' using 1:3 title "Floyd-Warshall" with linespoints lw 2 pt 7 lc rgb "red", \
     '' using 1:5 title "Dijkstra" with linespoints lw 2 pt 5 lc rgb "blue", \
     1e-4*(x**2) title "O(n^2)" with lines lw 2 lc rgb "black" dashtype 2

set output 'memory_complexity.png'
replot

print "Plots saved as time_complexity_visual.png and memory_usage_visual.png"

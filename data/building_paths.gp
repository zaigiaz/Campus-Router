set datafile separator whitespace
set style fill solid 1.0 border -1
set style data histograms
set xtics rotate by -45 nomirror
set boxwidth 0.8
set ylabel "Number of Shortest Paths Through Building"
set title "Building Centrality in University Shortest Paths"
set grid ytics

# Color palette for different buildings
set style histogram rowstacked gap 2

plot 'expirement_2.dat' using 1:xtic(2) title "Path Count" lc rgb"#4169E1" 

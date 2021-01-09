# Weakening Worms

After doing several [benchmarks](https://gist.github.com/cheeze2000/9250bf9966f15f40c0c91ec30c5234c7) on your server, you decided to do one last benchmark before you hit the bed. While you were waiting for the benchmark results, you fell asleep. You woke up the next day to find out that your servers have been infected by a worm overnight! \
Luckily, the worm did not attempt to steal any data but it repeatedly turned off a random server's connection to another server. Since it is a new type of worm that your antivirus has not seen before, your antivirus requires a very complicated report to learn more about the worm. \
\
The benchmarking tool keeps track of the timestamps when connections were unexpectedly closed (presumably by the worm). \
The report has to list down the wormfection score for every instant a connection was interrupted by the worm. For example, if a worm infects a cluster of `C` servers `(C <= N)`, the wormfection score would be `C²` for that particular cluster. The wormfection score for all your servers is simply the sum of all the scores of each cluster.

# Input
- A line consisting of a positive integer `N`, denoting the number of servers
- A line consisting of a positive integer `C`, denoting the number of connections in your network
- `C` lines consisting of the chronologically sorted connection interruptions in your network, with each line consisting of two positive integers:
    - a server number (`s0`)
    - a server number (`s1`)

# Output
-  A line consisting of `C` positive integers, each denoting the wormfection score of your entire network every time a connection is interrupted

# Examples
## Input
```
5
5
0 4
0 2
1 4
2 3
0 3
```

## Output
```
13 13 11 7 5
```

## Explanation
The first disconnect is `0 4`. The network forms 2 clusters, `1-4` and `0-2-3`. The wormfection score is `2² + 3² = 13`. \
The second disconnect is `0 2`. The network still forms the same clusters, `1-4` and `0-2-3`. The wormfection score is `13`. \
The third disconnect is `1 4`. The network now forms 3 clusters, `1`, `4` and `0-2-3`. The wormfection score is `1² + 1² + 3² = 11`. \
The fourth disconnect is `2 3`. The network now forms 4 clusters, `1`, `2`, `4`, `0-3`. The wormfection score is `1² + 1² + 1² + 2² = 7`. \
The fifth disconnect is `0 3`. The network now forms 5 clusters, every server not connected to any other server. The wormfection score is `1² + 1² + 1² + 1² + 1² = 5`. \
\
The wormfection scores should be non-ascending as the worms are weakening. \
The last wormfection score is always equal to `N`, the number of servers.
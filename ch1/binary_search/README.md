# Binary Search

## Compute time: O(Log N)

## Algorithm

Given a _sorted list_, `L` search for item `V`

1. Compare the middle value of list, `L` to `V`
2. If `L === V` => done
3. If `L < V` create new _sorted list_, `L_slice` from range 0:L-1; repeat 
4. if `L > V` create new _sorted list, `L_slice` from range L+1:end ; repeat


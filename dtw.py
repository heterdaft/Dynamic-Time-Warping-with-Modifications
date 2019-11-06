from point2d import Point2D

def distance(a1, a2):
    """ Finds the normal unmodified version of the dynamic time warping algorithm
    between two time series arrays """
    n = len(a1)
    m = len(a2)

    # Create a nxm sized matrix where all values are initialized to infinity
    DTW = [ [float("inf")] * m for i in range(n) ]
    DTW[0][0] = 0

    for i in range(n):
        for j in range(m):
            cost = __dist__(a1[i], a2[j])
            prev_i = i-1 if i>0 else 0  # If on the edges of the matrix do not
            prev_j = j-1 if j>0 else 0  #   use negative indices
            min_previous = min( DTW[prev_i][      j],
                                DTW[     i][ prev_j],
                                DTW[prev_i][ prev_j])
            DTW[i][j] = cost + min_previous
    return DTW[n-1][m-1]

def __dist__(point1, point2):
    """ Distance function currently being used for the dtw_distance calculations """
    # Use the Point2D to find the abs(point1-point2)
    return (point1 - point2).r

if __name__ == "__main__":
    print("Quick test in progress")
    a1 = [Point2D(0,0), Point2D(0,1), Point2D(0,2), Point2D(0,3)]
    a2 = [Point2D(1,0), Point2D(2,0), Point2D(3,0), Point2D(4,0)]
    print(distance(a1, a2))
    print(distance(a1, a1))

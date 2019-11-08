from point2d import Point2D
import math

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

def time_percentage(a1, time1, a2, time2):
    """ Finds the modified version of the dynamic time warping algorithm
    between two time series arrays and their given times. The two paths do not
    need to be of the same length or have the same timing signatures however this
    function has an O(nm) time complexity."""
    n = len(a1)
    m = len(a2)

    # Create a nxm sized matrix where all values are initialized to infinity
    DTW = [ [float("inf")] * m for i in range(n) ]
    DTW[0][0] = 0

    # Max distance is the largest penalty the combined cost can have
    MAX_DISTANCE = 5 # this value could be substituted with beta radius
    # Max aggregate distance is the worst possible combined cost
    MAX_AGGREGATE_DISTANCE = MAX_DISTANCE * n

    for i in range(n):
        for j in range(m):
            dist_cost = __dist__(a1[i], a2[j])
            time_cost = __time_cost__( max(time1[i], time2[j]) )
            total_cost = dist_cost + time_cost
            total_cost = MAX_DISTANCE if total_cost > MAX_DISTANCE else total_cost

            prev_i = i-1 if i>0 else 0  # If on the edges of the matrix do not
            prev_j = j-1 if j>0 else 0  #   use negative indices
            min_previous = min( DTW[prev_i][      j],
                                DTW[     i][ prev_j],
                                DTW[prev_i][ prev_j])

            DTW[i][j] = total_cost + min_previous
    return 1 - (DTW[n-1][m-1]/MAX_AGGREGATE_DISTANCE ) # Return a percentage of simularity

def basic_function(a1, a2, time):
    """ This basic function is not a DTW function but performs a basic comparison
    of two identically sized time series paths. An interpolation technique could
    be used to get the exact same number of samples at the same time if this method
    is used. Complexity is O(n) """
    n = len(time)
    MAX_DISTANCE = 5 # this value could be substituted with beta radius
    MAX_AGGREGATE_DISTANCE = MAX_DISTANCE * n
    aggregate_cost = 0
    for i in range(n):
        dist_cost = __dist__(a1[i], a2[i])
        time_cost = __time_cost__(time[i])
        total_cost = dist_cost + time_cost
        aggregate_cost += MAX_DISTANCE if total_cost > MAX_DISTANCE else total_cost
    return 1 - (aggregate_cost / MAX_AGGREGATE_DISTANCE)

def __dist__(point1, point2):
    """ Distance function currently being used for the distance calculations """
    # Use the Point2D to find the abs(point1-point2)
    return (point1 - point2).r

def __time_cost__( time ):
    """ Time cost function currently being used for distance calculations """
    time_cost = math.log(time/10)+1 # A suitable function should be found
    return time_cost if time_cost > 0 else 0

if __name__ == "__main__":
    print("Quick test in progress")
    a1 = [Point2D(0,0), Point2D(0,1), Point2D(0,2), Point2D(0,3)]
    a2 = [Point2D(1,0), Point2D(2,0), Point2D(3,0), Point2D(4,0)]
    print(distance(a1, a2))
    print(distance(a1, a1))

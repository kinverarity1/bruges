import unittest
import numpy
from agilegeo.attribute import compute_similarity

class SimilarityTest( unittest.TestCase ):

    def test_same_data( self ):
        """
        Simple test to check if the algorithm works for the
        trivial case.
        """
        data = numpy.zeros( [100, 100] ) 
        check_data = data + 1.0
        
        data +=10.
        window_size = 20

    
        output = compute_similarity( data, window_size )

        same = numpy.allclose( check_data[:,1:], 
                               output[:,1:], .001 )
        
        self.assertTrue( same )

    def test_stepout( self ):

        data = numpy.zeros( [ 100,100 ] )
        check_data = data + 1.0

        # Make adjacent traces dissimilar, next nearest trace
        # similar
        data += 11.
        data[ :,::2] = -11.0

        window_size = 20
        step_out = 2


        # Check with a step out of 2
        output = compute_similarity( data, window_size,
                                     step_out = step_out )
        

        same = numpy.allclose( check_data[:,step_out:], 
                               output[:,step_out:], .001 )
            
        self.assertTrue( same )

        # Check with a step out of 1
        step_out = 1
        output = compute_similarity( data, window_size,
                                     step_out = step_out )
        

        # Everything should be zero
        check_data -= 1
        same = numpy.allclose( check_data[:,step_out:], 
                               output[:,step_out:], .001 )
            
        self.assertTrue( same )


    def test_lag( self ):

        data = numpy.zeros( [ 100,100 ] )
        check_data = data + 1.0

        # Make an off by 1 similarity that can be corrected
        # with lag
        data[::2,::2] = -11.
        data[1::2,1::2]=-11

        lag = 1
        window_size = 20
        
        output = compute_similarity( data, window_size,
                                     lag=lag )

        same = numpy.allclose( check_data[:,1:], 
                               output[:,1:], .001 )

        self.assertTrue( same )
        
        # Should be zero with no lag
        lag = 0
        window_size = 20
        
        output = compute_similarity( data, window_size,
                                     lag=lag )

        check_data[:,1:] -= 1.
        same = numpy.allclose( check_data[:,1:], 
                               output[:,1:], .001 )

        self.assertTrue( same )
        
if __name__ == '__main__':
    unittest.main()
    

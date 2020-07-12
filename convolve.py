import scipy.stats

p = np.vectorize(scipy.stats.p, signature='(n),(n)->(),()')

p([[0, 1, 2, 3]], [[1, 2, 3, 4], [4, 3, 2, 1]])
(array([ 1., -1.]), array([ 0.,  0.]))

convolve = np.vectorize(np.convolve, signature='(n),(m)->(k)')

convolve(np.eye(4), [1, 2, 1])
array([[1., 2., 1., 0., 0., 0.],
       [0., 1., 2., 1., 0., 0.],
       [0., 0., 1., 2., 1., 0.],
       [0., 0., 0., 1., 2., 1.]])

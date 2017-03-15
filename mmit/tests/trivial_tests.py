"""
    MMIT: Max Margin Interval Trees
    Copyright (C) 2017 Toby Dylan Hocking, Alexandre Drouin
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import numpy as np

from numpy import infty as inf
from unittest import TestCase

from ..core import solver


class TrivialTests(TestCase):
    def setUp(self):
        self.target = [(-1, np.infty),
                       (-2, 3),
                       (-np.infty, 1)]
        self.target_lower, self.target_upper = zip(*self.target)
        self.target_lower = np.array(self.target_lower)
        self.target_upper = np.array(self.target_upper)


        self.features = np.array([-2.2, 3, 10])

    def test_1(self):
        """
        margin=0 yields total cost 0
        """
        margin = 0.0
        moves, preds, costs = solver.compute_optimal_costs(self.features, self.target_lower, self.target_upper, margin, 0)
        np.testing.assert_allclose(preds, [inf, 1, 0])
        np.testing.assert_allclose(costs, [0, 0, 0])

    def test_2(self):
        """
        margin=0.5 yields total cost 0
        """
        margin = 0.5
        moves, preds, costs = solver.compute_optimal_costs(self.features, self.target_lower, self.target_upper, margin, 0)
        np.testing.assert_allclose(preds, [inf, 1, 0])
        np.testing.assert_allclose(costs, [0, 0, 0])

    def test_3(self):
        """
        margin=1 yields total cost 0
        """
        margin = 1.0
        moves, preds, costs = solver.compute_optimal_costs(self.features, self.target_lower, self.target_upper, margin, 0)
        np.testing.assert_allclose(preds, [inf, 1, 0])
        np.testing.assert_allclose(costs, [0, 0, 0])

    def test_4(self):
        """
        margin=1.5 yields total cost 1
        """
        margin = 1.5
        moves, preds, costs = solver.compute_optimal_costs(self.features, self.target_lower, self.target_upper, margin, 0)
        np.testing.assert_allclose(preds, [inf, 1, 0])
        np.testing.assert_allclose(costs, [0, 0, 1])

    def test_5(self):
        """
        margin=2 yields total cost 2
        """
        margin = 2
        moves, preds, costs = solver.compute_optimal_costs(self.features, self.target_lower, self.target_upper, margin, 0)
        np.testing.assert_allclose(preds, [inf, 1, 0.5])
        np.testing.assert_allclose(costs, [0, 0, 2])


if __name__ == "__main__":
    pass
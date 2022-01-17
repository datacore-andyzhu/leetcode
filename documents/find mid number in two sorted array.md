```c++
#include <bits/stdc++.h> // added every header file :D
using namespace std;

// The method to compute the median of two sorted Arrays
// Input: vector A and vector B
// Output: median
float findMedianLogarithmic(vector<int> A, vector<int> B)
{

	// get the size of A and B
	int aSize = A.size();
	int bSize = B.size();

	/* if either of the two input arrays are empty then the median
	 will be middle elemnt of the array which is not empty
	 For example: A = {} and B = {1, 2, 6, 9, 13}
	 The median is 3rd element of B, which is 6
	 */
	if (aSize == 0)
	{ // A is empty

		if (bSize & 1)
		{ /* if bSize if odd the median is the middle element*/
			return B[(bSize / 2)];
		}
		else
		{ /* if bSize is even the median is the average of two middle elements*/
			return ((double)B[(bSize / 2)] + B[(bSize / 2) + 1]) / 2;
		}
	}
	else if (bSize == 0)
	{ // B is empty

		if (aSize & 1)
		{ /* if bSize if odd the median is the middle element*/
			return A[(aSize / 2)];
		}
		else
		{ /* if bSize is even the median is the average of two middle elements*/
			return ((double)A[(aSize / 2)] + A[(aSize / 2) + 1]) / 2;
		}
	}

	// to reduce the number of iterations it is efficient to perform
	// the binary search on the smaller array, hence we will keep the
	// shorter array in A
	if (aSize > bSize)
	{
		swap(A, B);
		swap(aSize, bSize);
	}

	int firstHalfSize = (aSize + bSize + 1) / 2;

	/**
	 * @brief Since A is the smaller array, it can contribute at
	 * least 0 values
	 * and at most, all of its values
	 */
	int minAContributes = 0;
	int maxAContributes = aSize;

	while (minAContributes <= maxAContributes)
	{
		int AContri = minAContributes + ((maxAContributes - minAContributes) / 2);
		int BContri = firstHalfSize - AContri;

		/*
			Check if AContri is the right contribution by A. If AContri is
			greater than 0, means if A contributes at least one value and hence
			B cannot contribute all of its value.
			Compare the last element contributed by A with next element to the last
			contributed	by B.
		*/
		if (AContri > 0 && A[AContri - 1] > B[BContri])
		{
			// Then it means A's contribution needs to be reduced
			// as p is greater than q'
			maxAContributes = AContri - 1;
		}

		/*
			Check if AContri is the right contribution by A. If AContri is
			smaller than A.length, means A does not contributes all of its
			values and hence B cannot contribute all of its value.
			Compare the last element contributed by A with next element to the last
			contributed	by B.
		*/
		else if (AContri < firstHalfSize && B[BContri - 1] > A[AContri])
		{
			// Then increase A's Contribution size
			// as q is greater than p', means q lies in the right half
			minAContributes = AContri + 1;
		}
		else
		{
			// we have the right contribution by A and B and all we need
			// is the last element of the left half

			// The left half end will be the largest value of the last
			// elements contributed by A and B
			int lastLeftHalf;
			if (AContri == 0) // if A's contribution is 0
				lastLeftHalf = B[BContri - 1];
			else if (BContri == 0) // if B is contributing 0 values
				lastLeftHalf = A[AContri - 1];
			else
				lastLeftHalf = max(A[AContri - 1], B[BContri - 1]);

			// we know that if the length of A U B is odd
			// then the median is last of element of half of A U B
			if ((aSize + bSize) & 1)
			{
				return lastLeftHalf;
			}

			/*
				If the length of A U B is even, then the median is average
				of two middle elements.
				The two middle elements are last of Left half and first of right
				half. We know the last of first half. The first of second half
				is computed as follows: if A contributes all of its values then
				first of right half is next element after last element B contributes
				which is B[BContri].
				if B Contributes all of its values then first of right half is A[AContri]
				Otherwise it the minimum of next elements after last elements contributed
				by A and B.
			*/
			int firstRightHalf;
			if (AContri == aSize)			 // A is contributing all of its values
				firstRightHalf = B[BContri]; // next element from B
			else if (BContri == bSize)		 // B is contributing all of its values
				firstRightHalf = A[AContri]; // next element from A
			else
				firstRightHalf = min(A[AContri], B[BContri]);

			return (lastLeftHalf + firstRightHalf) / 2.0;
		}
	}
	return -1.0;
}

// Driver program
int main()
{
	// test case 1
	vector<int> A{2, 5, 8, 9};
	vector<int> B{1, 3, 6};

	cout << "The median of A and B is " << findMedianLogarithmic(A, B) << endl;

	return 0;
}
```


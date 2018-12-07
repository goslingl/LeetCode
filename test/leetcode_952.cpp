struct union_find {
    vector<int> parent;
    vector<int> size;
    vector<uint8_t> rank;

    union_find(int n = 0) {
        if (n > 0)
            init(n);
    }

    void init(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1);
        size.resize(n + 1);

        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
            rank[i] = 0;
        }
    }

    int find(int x) {
        return x == parent[x] ? x : parent[x] = find(parent[x]);
    }

    bool unite(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y)
            return false;

        if (rank[x] < rank[y])
            swap(x, y);
        else if (rank[x] == rank[y])
            rank[x]++;

        parent[y] = x;
        size[x] += size[y];
        return true;
    }
};


vector<int> smallest_factor;
vector<bool> prime;
vector<int> primes;

void sieve(int maximum) {
    assert(maximum > 0);
    smallest_factor.assign(maximum + 1, 0);
    prime.assign(maximum + 1, true);
    prime[0] = prime[1] = false;
    primes = {2};

    for (int p = 2; p <= maximum; p += 2) {
        prime[p] = p == 2;
        smallest_factor[p] = 2;
    }

    for (int p = 3; p * p <= maximum; p += 2)
        if (prime[p])
            for (int i = p * p; i <= maximum; i += 2 * p)
                if (prime[i]) {
                    prime[i] = false;
                    smallest_factor[i] = p;
                }

    for (int p = 3; p <= maximum; p += 2)
        if (prime[p]) {
            smallest_factor[p] = p;
            primes.push_back(p);
        }
}


const int A_MAX = 1e6 + 5;

class Solution {
public:
    int largestComponentSize(vector<int>& A) {
        sieve(A_MAX);
        int n = A.size();
        union_find uf(n);
        vector<int> representative(A_MAX, -1);

        for (int i = 0; i < n; i++)
            while (A[i] > 1) {
                int p = smallest_factor[A[i]];

                do {
                    A[i] /= p;
                } while (A[i] % p == 0);

                if (representative[p] == -1)
                    representative[p] = i;
                else
                    uf.unite(i, representative[p]);
            }

        int largest = 0;

        for (int i = 0; i < n; i++)
            largest = max(largest, uf.size[uf.find(i)]);

        return largest;
    }
};

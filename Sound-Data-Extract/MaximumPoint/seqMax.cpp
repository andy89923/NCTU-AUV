#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f

int n;
vector<double> a, b;
vector<int> smt_a, smt_b;
vector<int> ans;

void init() {
	ans.clear();

	a.clear();
	b.clear();
	smt_a.clear();
	smt_b.clear();
}

void process() {
	n = (int) a.size();

	smt_a.push_back(-1);
	for (int i = 1; i < n; i++) {
		if (a[i-1] < a[i] && a[i] > a[i+1]) smt_a.push_back(i);
		if (b[i-1] < b[i] && b[i] > b[i+1]) smt_b.push_back(i);
	}
	smt_a.push_back(INF);
	cout << "A's Size = " << smt_a.size() << ", B's Size = " << smt_b.size() << '\n';

	for (auto tar : smt_b) {
		auto poi = upper_bound(smt_a.begin(), smt_a.end(), tar);

		int bac = *(poi); poi--;
		int fro = *(poi);

		// cout << fro << ' ' << tar << ' ' << bac << '\n';
		if (fro ==  -1) { 
			// cout << bac - tar << '\n'; 
			ans.push_back(bac - tar); 
			continue;
		}
		if (bac == INF) { 
			// cout << tar - fro << '\n'; 
			ans.push_back(fro - tar); 
			continue;
		}
		if (bac - tar > tar - fro) {
			ans.push_back(fro - tar);
		} else {
			ans.push_back(bac - tar);
		}
		// cout << min(bac - tar, tar - fro) << '\n';
	}	
}

int main() {
	// cin.tie(0), cout.sync_with_stdio(false);

	ifstream cin;
	for (int fil = -90; fil <= 90; fil += 30) {
		cout << "Processing on " << fil << "...\n";

		cin.open("./../Data/NewData VOL2/N_" + to_string(fil) + "l.txt");
		if (!cin){
			cout << "Unable to open file" << endl;
			exit(-1);
		}
		init();

		double x, y;
		while (cin >> x >> y) {
			a.push_back(x);
			b.push_back(y);
		}
		process();

		ofstream file_cout("./Results/" + to_string(fil) + ".txt");
		for (auto i : ans) file_cout << i << '\n';

		cin.close();
	}
	return 0;
}
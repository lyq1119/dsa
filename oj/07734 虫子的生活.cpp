#include <iostream>
#include <vector>
using namespace std;

int find(int i, vector<int>& parent, vector<int>& typetag){
    if (parent[i] == i){
        return i;
    } 
    int origin_parent = parent[i];
    int res = find(parent[i],parent,typetag);
    parent[i] = res;
    typetag[i] = (typetag[i]+typetag[origin_parent]+2)%2;
    return res;
}

bool check(int i, int j, vector<int>& parent, vector<int>& typetag){
    int x = find(i,parent,typetag);
    int y = find(j,parent,typetag);
    if (x != y){
        parent[y] = x;
        typetag[y] = (typetag[i]+typetag[j]+1+2)%2;
        return true;
    }
    if (typetag[i] != typetag[j]){
        return true;
    }
    return false;
}

bool fun(int i){
    int n,m;
    cout << "Scenario #" << i << ":" << endl;
    cin >> n >> m;

    vector<int> parent(n);
    vector<int> typetag(n,0);
    bool verdict{true};

    for (int i = 0; i < n; i++){
        parent[i] = i;
    }

    for (int k = 0; k < m; k++){
        int i,j;
        cin >> i >> j;
        if (!verdict){
            continue;
        }
        i -= 1;
        j -= 1;
        if (!check(i,j,parent,typetag)){
            verdict = false;
        }
    }
    return verdict;
}

int main(){
    int num_times;
    cin >> num_times;

    for (int i = 1; i < num_times+1; i++){
        if (fun(i)){
            cout << "No suspicious bugs found!" << endl;
        } else {
            cout << "Suspicious bugs found!" << endl;
        }
        if (i != num_times){
            cout << '\n';
        } 
    }
    return 0;
}
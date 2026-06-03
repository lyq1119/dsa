#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int a_test_case(){
    long long n, m, num, total{0};
    cin >> n >> m;

    vector<int> num_avai(m);
    vector<int> houzhuihe(m+1,0);
    for (int j = 0; j < m; j++){
        cin >> num;
        num_avai[j] = num;
    }

    sort(num_avai.begin(), num_avai.end());

    for (int j = m-1; j >= 0; j--){
        houzhuihe[j] = houzhuihe[j+1]+num_avai[j];
    }

    int m1;
    if (num_avai[m-1] < n){
        m1 = m;
    } else {
        for (int j = m-1; j >= 0; j--){
            if (num_avai[j] >= n){
                m1 = j;
            } else {
                break;
            }
        }
    }

    total += (n-1)*(m-m1)*(m-m1-1);
    total += ((houzhuihe[0]-houzhuihe[m1])*2)*(m-m1);

    if (m1 == 0){
        return total;
    }

    int zhizhen{m1};
    int b = num_avai[zhizhen-1];
    
    for (int i = 0; i < m1; i++){

        int a = num_avai[i];
        if (2*a >= n){
            total += 2*(houzhuihe[i+1]-houzhuihe[m1]);
            total += 2*(a-n+1)*(m1-i-1);
            continue;
        }
        if (b+a >= n){
            while (b+a >= n){
                zhizhen -= 1;
                b = num_avai[zhizhen];
            }
            zhizhen += 1;
        }
        
        total += 2*(houzhuihe[zhizhen]-houzhuihe[m1]);
        total += 2*(a-n+1)*(m1-zhizhen);
    }
    return total;
}

int main(){
    int num_cases;
    cin >> num_cases;
    for (int i = 0; i < num_cases; i++){
        cout << a_test_case() << endl;
    }
}
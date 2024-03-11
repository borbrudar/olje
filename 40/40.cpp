#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef std::deque<ull> di;
typedef std::vector<ull> vi;
typedef std::pair<ull,ull> pr;
typedef std::vector<pr> vii;
#define rep(i,n) for(ull i = 0; i < n; i++)
#define aull(n) n.begin(), n.end()
const int mod = 1e9 + 7;
const ull INF = 2 * 1e18 + 100;
const int inf = 1e9;
 
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
 
    //int q=1; //cin >> q;
    vector<ll> q = {1,10,100,1'000,10'000,100'000,1'000'000};
    ll cur = 1;
    for(ll k : q){
        //ull k; cin >> k;
        ull digitNum = 1,digitsBefore = 0, dnow = 0;
        for(int i = 1; i <= 18;i++) {
            dnow += ((ull)pow(10,i) - (ull)pow(10,i-1))*i;
            if(dnow >= k){
                digitNum = i;
                break;
            }
            digitsBefore = dnow;
        }
 
        ull top = (ull)pow(10,digitNum) -1;
        ull bot = (ull)pow(10,digitNum -1);
        ull mid = (top + bot)/2;
        ull ans = 0,ansi = 0;
        ull start = bot;
        while(bot <= top){
            mid = (top + bot)/2;
            ull ind = digitNum * (mid - start) + digitsBefore + 1;
 
            if(ind <= k) {
                bot = mid + 1;
                if(mid > ans){
                    ansi = ind;
                    ans = mid;
                }
            }else top = mid - 1;
        }
        string s = to_string(ans);
        cur = cur*(s[k-ansi]-'0');
    }    
   cout<<cur<<"\n";
}
 
/*
 
123456789 10 11 12 13 14 151617181920
 
*/
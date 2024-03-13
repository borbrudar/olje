#include <bits/stdc++.h>
 
using namespace std;
typedef long long ll;
 
void solve(){
    vector<int> p(1e9+100,1);
    p[0]=p[1]=0;
    for(int i =2;i<p.size();i++){
        if(!p[i]) continue;
        for(int j=i*2;j<p.size();j+=i) p[j]=0;
    }


    vector<ll> vec = {1};
    int side =2;
    int cnt =0;
    for(int i =0 ;i< (1e6);i++){
        vec.push_back(vec.back()+side);
        if(p[vec.back()]) cnt++;
        vec.push_back(vec.back()+side);
        if(p[vec.back()]) cnt++;
        vec.push_back(vec.back()+side);
        if(p[vec.back()]) cnt++;
        vec.push_back(vec.back()+side);
        if(p[vec.back()]) cnt++;
        
        if(cnt/((float)vec.size()) < 0.1f){
            cout<<cnt/((float)vec.size())<<"\n";
            cout<<side+1;
            break;
        } 
        side+=2;
    }
}
 
int main(){
    ios_base::sync_with_stdio(0),cin.tie(0);
    int t=1;//cin>>t;
    while(t--) solve();
}
 
/*
*/
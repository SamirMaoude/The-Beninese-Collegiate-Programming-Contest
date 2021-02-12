#include<bits/stdc++.h>


using namespace std;

bool colored[1001][1001];

int main ()
{


    ios_base::sync_with_stdio(false); cin.tie(NULL);

    freopen("paint.in", "r",stdin);

    memset(colored, 0 , sizeof(colored));

    int N,M,Q;

    scanf("%d %d %d", &N, &M, &Q);

    for(int i = 0; i < Q; i++)
    {
        int x, y;

        scanf("%d %d", &x, &y);

        colored[x][y]=!colored[x][y];

        
        colored[x-1][y] = !colored[x-1][y];

        colored[x+1][y] = !colored[x+1][y];

        colored[x][y+1] = !colored[x][y+1];

        colored[x][y-1] = !colored[x][y-1];
    }


    for (int i =1; i<=N; i++)
    {
        for(int j=1; j<=M; j++)
        {
            if( j<M)
            printf("%d ", colored[i][j]);
            else
            printf("%d", colored[i][j]);
        }
        puts("");
    }

}
#include <stdio.h>
#include <stdlib.h>

int niyuan(int a,int m)
{
    int c=1;

    while(a*c%m!=1){
        c++;
    }
    return c;
}

void x2tool(int a,int m,int t[10])
{
    int k=0;
    for(int i=1;i<m;i++){
        if((a+m)%m==i*i%m){
            t[k]=i;
            k++;
            if(k==10) break;
        }
    }
}

int mod(int a,int c,int m)
{
    int less=1;
    for(int i=0;i<c;i++){
        less=a*less%m;
    }
    return less;
}

int main()
{
    while(1)
    {
        printf("请选择需要的功能：1.求模 2.求逆元 3.求x^2=a mod m的两个解 4.退出\n");
        int f;
        scanf("%d",&f);
        if(f==1){
            printf("请输入a^c mod m中的a,c,m：");
            int a,c,m;
            scanf("%d%d%d",&a,&c,&m);
            int d;
            d=mod(a,c,m);
            printf("%d^%d mod %d=%d\n",a,c,m,d);
        }else if(f==2){
            printf("请输入a*c=1 mod m中的a,m：");
            int a,m;
            scanf("%d%d",&a,&m);
            int c;
            c=niyuan(a,m);
            printf("%d*%d=1 mod %d\n",a,c,m);
        }else if(f==3){
            printf("请输入x^2=a mod m中的a,m：");
            int a,m;
            scanf("%d%d",&a,&m);
            int t[10]={0};
            x2tool(a,m,t);
            printf("解为：");
            for(int i=0;i<10;i++){
                if(t[i]!=0){
                    printf("t%d=%d  ",i+1,t[i]);
                }else break;
            }
            printf("\n");
        }else if(f==4) break;

    }

    return 0;
}

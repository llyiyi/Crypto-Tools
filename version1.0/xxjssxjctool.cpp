#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct yz
{
    int p;
    int num;
}yz;

int p[100];

int mod(int a,int c,int m);
int ifp(int p);
void parr(int m);
void fenjie(int m,yz* yz);
void yuangen(int m,int * g);
int niyuan(int a,int m);
void x2tool(int a,int m,int * t);
int ola(int m);
int gcd(int a,int b);

int gcd(int a,int b)
{
    if(a<b){
        a=a+b;
        b=a-b;
        a=a-b;
    }
    while(b!=0)
    {
        int temp=a%b;
        a=b;
        b=temp;
    }

    return a;
}

int ola(int m)
{
    int fai=m;
    yz yz[100]={{0,0}};
    fenjie(m,yz);

    for(int i=0;i<100;i++){
        if(yz[i].p==0) break;
        fai=fai*(yz[i].p-1)/yz[i].p;
    }

    return fai;
}

int ifp(int p)
{
    int f=1;

    for(int i=2;i<=sqrt(p);i++){
        if(p%i==0){
            f=0;
            break;
        } 
    }

    return f;
}

void parr(int m)
{
    int k=0;
    for(int i=2;i<=m;i++){
        if(ifp(i)) p[k++]=i;
    }
}

void fenjie(int m,yz* yz)
{
    int k=0;
    int q=0;
    parr(m);
    while(m!=1)
    {
       if(m%p[k]==0){
        yz[q].p=p[k];
        while(m%p[k]==0){
            m=m/p[k];
            yz[q].num++;
        }
        q++;
       }
       k++;
    }
}

void yuangen(int m,int * g)
{
    int k=0;
    int fai=ola(m);
    yz yz[100]={{0,0}};
    fenjie(fai,yz);

    for(int i=1;i<m;i++)
    {
        int f=0;
        for(int j=0;j<100;j++)
        {
            if(gcd(i,m)!=1) break;
            if(yz[j].p==0){f=1; break;}
            if(mod(i,fai/yz[j].p,m)==1) break;
        }
        if(f==1) g[k++]=i;
    }

}

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
        printf("请选择需要的功能：1.求模 2.求逆元 3.求x^2=a mod m的解 4.求模m的原根g 5.退出\n");
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
        }else if(f==4){
            printf("请输入m：");
            int m,g[100]={0};
            scanf("%d",&m);
            yuangen(m,g);
            int i=0;
            printf("原根为：");
            while(g[i]!=0)
            {
                printf("g%d=%d  ",i+1,g[i]);
                i++;
            }
            printf("\n");
        }else if(f==5) break; 

    }

    return 0;
}
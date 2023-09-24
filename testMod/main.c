#include <stdio.h>


int Gcd(int a,int m){
    int tmp;
    while(m){
        tmp = a%m;
        a = m;
        m = tmp;
    }
    return a;
}

void mod(int a,int b,int m){
    int gcd_num = Gcd(a,m);
    if(!(b%gcd_num)){//说明能整除
        int origin_answer=1,a1=a/gcd_num,b1=b/gcd_num,m1=m/gcd_num;
        while(a1*origin_answer%m-1){//ax=1modm必有唯一解
            origin_answer++;
        }
        int x;
        for(int i=0;i<gcd_num;i++){
            x=origin_answer*b1+i*m1;
            x=x%m;
            printf("%d ",x);
        }
    }
    else{
        printf("x 无解");
        return;
    }
}

int main(){
    int a,b,m;

    printf("找到符合要求的 x 的解");
    scanf("%d %d %d",&a,&b,&m);
    mod(a,b,m);

    return 0;
}
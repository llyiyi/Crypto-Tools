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
    if(!(b%gcd_num)){//˵��������
        int origin_answer=1,a1=a/gcd_num,b1=b/gcd_num,m1=m/gcd_num;
        while(a1*origin_answer%m-1){//ax=1modm����Ψһ��
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
        printf("x �޽�");
        return;
    }
}

int main(){
    int a,b,m;

    printf("�ҵ�����Ҫ��� x �Ľ�");
    scanf("%d %d %d",&a,&b,&m);
    mod(a,b,m);

    return 0;
}
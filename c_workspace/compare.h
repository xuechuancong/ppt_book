#define compare(a,b) ({ \ 
   if(a>b) \
       printf("a>b");\
   else if(a<b) \
       printf("a<b");\
   else \
       printf("a=b");})    

======Pointers=========
Pointer is a variable that stoes address of another value. It is pass by reference type.

1.  int a = 10;
    int *p = &a;    // That means a pointer 'p' is initiated to address of 'a'. And the value in the address can be accessed by using '*p'
    
    //we can asses elements of arr if pointer p is indicating it by using p[0],p[1],... so on.
2.  int arr[5]={1,2,3,4,5}
    int *p = arr    // Here we need not give *p = &arr. Beacause arr itself pointes to arr[0].
    print(*p +2)    // It prints arr[0] +2.
    print(*(p+2))   // It prints arr[0+2]
    print(p[2])     // prints arr[2]
    print(*p++)     // use value at p then move p forward. That prints arr[0]. Now pointer p is at arr[1]
    *p++ = (*p)++  //not correct 


3. p->a = (*p).a with struct.

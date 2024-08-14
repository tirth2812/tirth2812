//rect,circle,square=area
import java.util.*;
// Rectangle Class File
class prime_no {
    int i,j;
    void prime()
    {
        for(i=1;i<=100;i++)
        {
            for (j=i;j>2;j--)
            {
                if(i%j==0)
                {
                    break;
                }
            System.out.println(i);
            }
        }
    }
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);//scanner class sc is obj of scanner class
        prime_no obj = new prime_no();
        obj.prime();
    }
}

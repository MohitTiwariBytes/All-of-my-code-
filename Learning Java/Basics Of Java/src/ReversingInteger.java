import java.util.Scanner;


public class ReversingInteger {
    public static void main(String[] args) {
        int i;
        for(i=10;i!=-1;i--){
            System.out.println("You are currently " +i+" KiloMeters away from me:)");
            if(i == 0){
                System.out.println("Your location and my location is now same");
            }
        }
    }
}

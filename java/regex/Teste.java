public class Teste{

    public static void main(String[] args){

        String[] ips = new String[]{"127.0.0.1:8000", "127.0.0.1", "47/  5.  07 3 -   256  _ 73  : 8  75  3",
                                    "127_0-0.1:8000", "9 8509 7224", "meuip.hostfudida.gratis:666"};

        String regex2 = "((.*[\\d\\w]+.*)+[\\._\\-/]+)+[\\d\\w]*.*:*[.*[\\d\\w]*.*]*";

        for(String ip:ips){
            System.out.println(ip+"\n"+ip.matches(regex2));
        }
        
    }

}
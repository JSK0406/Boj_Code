import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        List<List<String>> lst = new ArrayList<>();

        for (int i = 0; i < 15; i++) {
            lst.add(new ArrayList<String>());
        }

        for (int i = 0; i < 5; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < tmp.length(); j++) {
                lst.get(j).add(String.valueOf(tmp.charAt(j)));
            }
        }

        for (int i = 0; i < 15; i++) {
            if (lst.size() == 0) {
                continue;
            } else {
                for (String str : lst.get(i)) {
                    System.out.print(str);
                }
            }
        }
    }
}
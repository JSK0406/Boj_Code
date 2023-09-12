import java.io.*;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Integer> map = new HashMap<>();

        int N = Integer.parseInt(br.readLine());
        int max = 0;
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            map.put(str, map.getOrDefault(str, 0) + 1);
            max = Integer.max(max, map.get(str));
        }
        List<String> arrList = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() == max) {
                arrList.add(entry.getKey());
            }
            Collections.sort(arrList);
        }
        System.out.println(arrList.get(0));
    }

}
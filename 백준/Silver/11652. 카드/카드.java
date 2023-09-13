import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Long, Integer> map = new HashMap<>();

        int N = Integer.parseInt(br.readLine().trim());
        int max = 0;
        for (int i = 0; i < N; i++) {
            Long num = Long.parseLong(br.readLine().trim());
            int cnt = map.getOrDefault(num, 0);
            map.put(num, cnt + 1);
            max = Integer.max(max, cnt + 1);
        }

        int ans = 0;
        List<Long> ArrList = new ArrayList<>();
        for (Map.Entry<Long, Integer> entry : map.entrySet()) {
            if (entry.getValue() == max) {
                ArrList.add(entry.getKey());
            }
        }
        Collections.sort(ArrList);
        System.out.println(ArrList.get(0));

    }
}
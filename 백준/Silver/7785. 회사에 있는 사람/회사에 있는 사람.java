import java.io.*;
import java.util.*;

public class Main  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        HashMap<String, String> hm = new HashMap<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String status = st.nextToken();
            hm.put(name, status);
        }

        ArrayList<String> lst = new ArrayList<>();

        for (String n : hm.keySet()) {
            String s = hm.get(n);
            if (s.equals("enter")) {
                lst.add(n);
            }
        }

        Collections.sort(lst, Collections.reverseOrder());

        for (String str : lst) {
            System.out.println(str);
        }
    }
}
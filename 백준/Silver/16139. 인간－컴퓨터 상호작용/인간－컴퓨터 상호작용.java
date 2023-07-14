import java.io.*;
import java.util.*;
import java.math.*;

public class Main  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        String str = br.readLine().strip();  // 받는 문장
        int q = Integer.parseInt(br.readLine());  // 질문 수

        int[][] arr = new int[str.length()]['z' - 'a' + 1];  // str의 인덱스마다 a~z까지 표시
        arr[0][str.charAt(0) - 'a']++;

        for (int sen = 1; sen < str.length(); sen++) {
            int nowAdd = str.charAt(sen) - 'a';
            for (int alp = 0; alp < 'z' - 'a' + 1; alp++) {
                if (alp == nowAdd) {
                    arr[sen][alp] = arr[sen-1][alp] + 1;
                } else {
                    arr[sen][alp] = arr[sen-1][alp];
                }
            }
        }


        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int findIdx = st.nextToken().charAt(0) - 'a';
            int start = Integer.parseInt(st.nextToken());
            int finish = Integer.parseInt(st.nextToken());
            if (start == 0) {
                bw.write(String.valueOf(arr[finish][findIdx]) + "\n");
            } else {
                bw.write(String.valueOf(arr[finish][findIdx] - arr[start - 1][findIdx]) + "\n");
            }

        }

        bw.flush();
        bw.close();
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<Integer> numList = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] rowArr = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                numList.add(Integer.parseInt(rowArr[j]));
            }
        }
        Collections.sort(numList);
        System.out.println(numList.get(N*N - N));
    }
}
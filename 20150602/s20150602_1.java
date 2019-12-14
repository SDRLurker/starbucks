import java.util.List;
import java.util.ArrayList;

public class s20150602_1 {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> r = new ArrayList<List<Integer>>();
        
        for(int i=1;i<=numRows;i++){
            List<Integer> one = new ArrayList<Integer>();
            for(int j=0;j<i;j++){
                if(j==0)    one.add(1);
                else if(j==i-1)     one.add(1);
                else {
                    List<Integer> bef = r.get(i-2);
                    one.add(bef.get(j-1)+bef.get(j));
                }
            }
            r.add(one);
        }
        return r;
    }
}

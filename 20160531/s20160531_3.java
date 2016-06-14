import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class s20160531_3 {


// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
interface NestedInteger {
    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    public boolean isInteger();
    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    public Integer getInteger();
    // @return the nested list that this NestedInteger holds, if it holds a nested list
    // Return null if this NestedInteger holds a single integer
    public List<NestedInteger> getList();
}

class NestedIterator implements Iterator<Integer> {
    List<Integer> values = new ArrayList<Integer>();
    int seq;
    
    private void insertList(List<NestedInteger> nestedList) {
         for(NestedInteger ni:nestedList) {
            if(ni.isInteger()){
                values.add(ni.getInteger());
            } else {
                insertList(ni.getList());
            }
        }
    }
    public NestedIterator(List<NestedInteger> nestedList) {
       insertList(nestedList);
    }
    /* iterator 사용법은 다음 사이트 참조 */
    /* http://egloos.zum.com/iilii/v/3788564 */
    @Override
    public Integer next() {
        return values.get(seq++);
    }

    @Override
    public boolean hasNext() {
        return seq < values.size();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */

}

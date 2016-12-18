<?php
/**
 * SoClass.php
 * 索引与搜索类  */
 
class SoClass {
 
    private $_xindex;
 
    private $_xsearch;
 
    private $_project;
 
    public function __construct($project){
 
        //载入引导文件
        require_once '/usr/local/xunsearch/sdk/php/lib/XS.php';
        //初始化
        $xs = new XS($project); 
        $this->_project = $project;
        $this->_xindex = $xs->index; 
        $this->_xsearch = $xs->search;
        $this->_xsearch->setCharset('UTF-8');
    }
 
    public function query($keyWord,$row=20,$jnum=0){
 
        $xs = new XS($this->_project);
        $xs->search->setFuzzy();
        $xs->search->setAutoSynonyms();
        $xs->search->setQuery($keyWord); //支持同义词搜索，默认打开
        $xs->search->setLimit($row, $jnum); //设置返回结果最多为 5 条，并跳过前 10 条
        $docs = $xs->search->search(); //执行搜索，将搜索结果文档保存在 $docs 数组中        
        $count = $xs->search->count(); //获取搜索结果的匹配总数估算值
        if($count){
            $data = array();
            foreach ($docs as $key=>$doc){
                $data[$key]['pid'] = $doc->pid;
                $data[$key]['nid'] = $doc->nid;
                $data[$key]['category'] = $doc->category;
                $data[$key]['url'] = $doc->url;
                $data[$key]['name'] = $xs->search->highlight(htmlspecialchars($doc->name));
                $data[$key]['message'] = $xs->search->highlight(htmlspecialchars($doc->message));
            }
 
            return array('data'=>$data,'count'=>$count);
        }
        return array();
    }
 
    public function hotWord($num,$type='lastnum'){
 
        return $this->_xsearch->getHotQuery($num,$type);
    }
 
    public function expanded($keyWord){
 
        return $this->_xsearch->getExpandedQuery($keyWord);
    }
 
    public function lastCount(){
 
        return $this->_xsearch->getLastCount();
    }
 
    public function index($data,$update=0){
 
        // 创建文档对象
        $doc = new XSDocument;
        $doc->setFields($data);
 
        // 添加或更新到索引数据库中
        if(!$update){
            $this->_xindex->add($doc);
        }else{
            $this->_xindex->update($doc);
        }
    }
 
    public function delete($idArray){
 
        //删除索引(主键删除array('1','2','3'))
        $this->_xindex->del($idArray); 
    }
 
    public function addSynonym($word1,$word2){
 
        $this->_xindex->addSynonym($word1,$word2);
    }
 
    public function clearIndex(){
 
        $this->_xindex->clean();
    }
 
}
 
?>
http://www.jb51.net/article/40341.htm  验证码类




访问基本控制器：Route::get('home/index', 'Home\IndexController@index');

分配数据
在控制器里：return view('home/index', ['key' => 'value']);
在视图里：Route::get('home/index', 'Home\IndexController@index');
模板：{{ $key }}


--------------------------------跟model层配合使用-----------------------------
model层
namespace App\Http\Model;

use Illuminate\Database\Eloquent\Model;

class Index extends Model
{
    protected $table = 'wolf_user';//指定表名
    protected $primaryKey='id';//指定主键
    public $timestamps=false;//表明模型是否应该被打上时间戳
    // protected $guarded=[];

    
}


Controllers层
namespace App\Http\Controllers\Home;
use App\Http\Controllers\Controller;
use DB;
use App\Http\Model\Index;


class IndexController extends Controller
{
    public function index()
    {
    	// $users = DB::select("select * from wolf_user");
    	$count = Index::all()->avg('id');//返回所有 --mysql里的函数都可以用
    	$users = Index::where('id','>',10)->orderBy('username', 'desc')
               ->take(10)
               ->get();

         $test = Index::where('id','>',70)->lists('username','id');//返回一个一维数组
        return view('home/index', ['users' => $users,'count' => $count,'test' => $test]);
    }
}



引入css
href="{{asset('resources/views/admin/style/font/css/font-awesome.min.css')}}

{{url('admin/code')}}


layer.layui.com  //弹窗库

www.uploadify.com //异步上传组件  36集
except()//除了谁

return redirect('admin/index')//重定向

return back()->with('errors','提示文字')；//回退到上一步
import r2020.den1.module


r2020.den1.module.func()



##########
from r2020.den1.module import func, func2

func()

########
import r2020.den1.module as module
import r2020.den1.module2 as module2

module.func()
module.func2()

module2.func()


########
from r2020.den1.module import func as mod_func, func2 as mod_func2
from r2020.den1.module2 import func as mod2_func, func2 as mod2_func2

mod_func()
mod2_func()

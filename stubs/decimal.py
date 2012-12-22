# NOTE: At least two things need to be discussed:
# *) should we use class Decimal<t>; t __abs__(t self, ...)-style definitions?
# *) what should we do when we have a definition like: __abs__(self, round=True, context=None)? The only way to make __abs(self, context=Blablabla) work is to override the default defaults (dirty).

# TODO need MyPy support for "threading"/"_thread" + "complex" + collections.namedtuple
import builtins
import collections

Context BasicContext
class Clamped(DecimalException): pass
class ConversionSyntax(InvalidOperation): pass
class Context(builtins.object):
  int prec
  str rounding # TODO enum?
  list<DecimalException> traps
  list<DecimalException> flags
  int Emin
  int Emax
  int capitals
  int clamp
  int Etiny(Context self): pass
  int Etop(Context self): pass
  Context __copy__(Context self): pass
  void __init__(Context self): pass
  void __init__(Context self, int prec, str rounding): pass
  void __init__(Context self, int prec, str rounding, list<DecimalException> traps): pass
  void __init__(Context self, int prec, str rounding, list<DecimalException> traps, list<DecimalException> flags): pass
  void __init__(Context self, int prec, str rounding, list<DecimalException> traps, list<DecimalException> flags, int Emin): pass
  void __init__(Context self, int prec, str rounding, list<DecimalException> traps, list<DecimalException> flags, int Emin, int Emax): pass
  void __init__(Context self, int prec, str rounding, list<DecimalException> traps, list<DecimalException> flags, int Emin, int Emax, int capitals): pass
  void __init__(Context self, int prec, str rounding, list<DecimalException> traps, list<DecimalException> flags, int Emin, int Emax, int capitals, int clamp): pass
  void __init__(Context self, int prec, str rounding, list<DecimalException> traps, list<DecimalException> flags, int Emin, int Emax, int capitals, int clamp, any _ignored_flags): pass
  str __repr__(Context self): pass
  Decimal abs(Context self, Decimal a): pass
  Decimal add(Context self, Decimal a, Decimal b): pass
  Decimal canonical(Context self, Decimal a): pass
  void clear_flags(Context self): pass
  Decimal compare(Context self, Decimal a, Decimal b): pass
  Decimal compare(Context self, int a, int b): pass
  Decimal compare(Context self, Decimal a, int b): pass
  Decimal compare(Context self, int a, Decimal b): pass
  Decimal compare_signal(Context self, Decimal a, Decimal b): pass
  Decimal compare_signal(Context self, int a, int b): pass
  Decimal compare_signal(Context self, Decimal a, int b): pass
  Decimal compare_signal(Context self, int a, Decimal b): pass
  Decimal compare_total(Context self, Decimal a, Decimal b): pass
  Decimal compare_total(Context self, int a, int b): pass
  Decimal compare_total(Context self, Decimal a, int b): pass
  Decimal compare_total(Context self, int a, Decimal b): pass
  Decimal compare_total_mag(Context self, Decimal a, Decimal b): pass
  Decimal compare_total_mag(Context self, int a, int b): pass
  Decimal compare_total_mag(Context self, Decimal a, int b): pass
  Decimal compare_total_mag(Context self, int a, Decimal b): pass
  Context copy(Context self): pass
  Decimal copy_abs(Context self, Decimal a): pass
  Decimal copy_abs(Context self, int a): pass
  Decimal copy_decimal(Context self, int a): pass
  Decimal copy_decimal(Context self, Decimal a): pass
  Decimal copy_negate(Context self, Decimal a): pass
  Decimal copy_negate(Context self, int a): pass
  Decimal copy_sign(Context self, Decimal a): pass
  Decimal copy_sign(Context self, int a): pass
  Decimal create_decimal(Context self, str num): pass
  Decimal create_decimal(Context self, float num): pass
  Decimal create_decimal(Context self, int num): pass
  Decimal create_decimal(Context self, Decimal num): pass  
  Decimal create_decimal_from_float(float f): pass
  Decimal create_decimal_from_float(int f): pass
  Decimal divide(Context self, Decimal a, Decimal b): pass
  Decimal divide(Context self, int a, int b): pass
  Decimal divide(Context self, Decimal a, int b): pass
  Decimal divide(Context self, int a, Decimal b): pass
  Decimal divide_int(Context self, Decimal a, Decimal b): pass
  Decimal divide_int(Context self, int a, int b): pass
  Decimal divide_int(Context self, Decimal a, int b): pass
  Decimal divide_int(Context self, int a, Decimal b): pass
  Decimal divmod(Context self, Decimal a, Decimal b): pass
  Decimal divmod(Context self, int a, int b): pass
  Decimal divmod(Context self, Decimal a, int b): pass
  Decimal divmod(Context self, int a, Decimal b): pass
  Decimal exp(Context self, Decimal a): pass
  Decimal exp(Context self, int a): pass

  Decimal fma(Context self, Decimal a, Decimal b, Decimal c): pass
  Decimal fma(Context self, int a, int b, int c): pass
  Decimal fma(Context self, int a, Decimal b, int c): pass
  Decimal fma(Context self, Decimal a, int b, Decimal c): pass
  Decimal fma(Context self, Decimal a, Decimal b, int c): pass
  Decimal fma(Context self, int a, Decimal b, Decimal c): pass
  Decimal fma(Context self, Decimal a, int b, int c): pass
  Decimal fma(Context self, int a, int b, Decimal c): pass

  bool is_canonical(Context self, Decimal a): pass
  bool is_finite(Context self, Decimal a): pass
  bool is_finite(Context self, int a): pass
  bool is_infinite(Context self, Decimal a): pass
  bool is_infinite(Context self, int a): pass
  bool is_nan(Context self, Decimal a): pass
  bool is_nan(Context self, int a): pass
  bool is_normal(Context self, int a): pass
  bool is_normal(Context self, Decimal a): pass
  bool is_qnan(Context self, Decimal a): pass
  bool is_qnan(Context self, int a): pass
  bool is_signed(Context self, Decimal a): pass
  bool is_signed(Context self, int a): pass
  bool is_snan(Context self, Decimal a): pass
  bool is_snan(Context self, int a): pass
  bool is_subnormal(Context self, int a): pass
  bool is_subnormal(Context self, Decimal a): pass
  bool is_zero(Context self, Decimal a): pass
  bool is_zero(Context self, int a): pass
  Decimal ln(Context self, Decimal a): pass
  Decimal ln(Context self, int a): pass
  Decimal log10(Context self, Decimal a): pass
  Decimal log10(Context self, int a): pass
  Decimal logb(Context self, Decimal a): pass
  Decimal logb(Context self, int a): pass

  Decimal logical_and(Context self, Decimal a, Decimal b): pass
  Decimal logical_and(Context self, int a, int b): pass
  Decimal logical_and(Context self, Decimal a, int b): pass
  Decimal logical_and(Context self, int a, Decimal b): pass

  Decimal logical_invert(Context self, Decimal a): pass
  Decimal logical_invert(Context self, int a): pass

  Decimal logical_or(Context self, int a, int b): pass
  Decimal logical_or(Context self, Decimal a, Decimal b): pass
  Decimal logical_or(Context self, int a, Decimal b): pass
  Decimal logical_or(Context self, Decimal a, int b): pass

  Decimal logical_xor(Context self, int a, int b): pass
  Decimal logical_xor(Context self, Decimal a, Decimal b): pass
  Decimal logical_xor(Context self, int a, Decimal b): pass
  Decimal logical_xor(Context self, Decimal a, int b): pass
  Decimal max(Context self, Decimal a, Decimal b): pass
  Decimal max(Context self, int a, int b): pass
  Decimal max(Context self, Decimal a, int b): pass
  Decimal max(Context self, int a, Decimal b): pass
  Decimal max_mag(Context self, int a, int b): pass
  Decimal max_mag(Context self, Decimal a, Decimal b): pass
  Decimal max_mag(Context self, int a, Decimal b): pass
  Decimal max_mag(Context self, Decimal a, int b): pass
  Decimal min(Context self, Decimal a, Decimal b): pass
  Decimal min(Context self, int a, int b): pass
  Decimal min(Context self, Decimal a, int b): pass
  Decimal min(Context self, int a, Decimal b): pass
  Decimal min_mag(Context self, int a, int b): pass
  Decimal min_mag(Context self, Decimal a, Decimal b): pass
  Decimal min_mag(Context self, int a, Decimal b): pass
  Decimal min_mag(Context self, Decimal a, int b): pass
  Decimal minus(Context self, Decimal a): pass
  Decimal minus(Context self, int a): pass
  Decimal multiply(Context self, Decimal a, Decimal b): pass
  Decimal multiply(Context self, int a, int b): pass
  Decimal multiply(Context self, int a, Decimal b): pass
  Decimal multiply(Context self, Decimal a, int b): pass
  Decimal next_minus(Context self, Decimal a): pass
  Decimal next_minus(Context self, int a): pass
  Decimal next_plus(Context self, Decimal a): pass
  Decimal next_plus(Context self, int a): pass
  Decimal next_toward(Context self, int a, int b): pass
  Decimal next_toward(Context self, Decimal a, Decimal b): pass
  Decimal next_toward(Context self, int a, Decimal b): pass
  Decimal next_toward(Context self, Decimal a, int b): pass
  Decimal normalize(Context self, Decimal a): pass
  Decimal normalize(Context self, int a): pass
  str number_class(Context self, int a): pass
  str number_class(Context self, Decimal a): pass
  Decimal plus(Context self, Decimal a): pass
  Decimal plus(Context self, int a): pass
  Decimal power(Context self, int a, int b): pass
  Decimal power(Context self, Decimal a, Decimal b): pass
  Decimal power(Context self, Decimal a, int b): pass
  Decimal power(Context self, int a, Decimal b): pass
  Decimal power(Context self, int a, int b, int modulo): pass
  Decimal power(Context self, Decimal a, Decimal b, int modulo): pass
  Decimal power(Context self, Decimal a, int b, int modulo): pass
  Decimal power(Context self, int a, Decimal b, int modulo): pass
  Decimal power(Context self, int a, int b, Decimal modulo): pass
  Decimal power(Context self, Decimal a, Decimal b, Decimal modulo): pass
  Decimal power(Context self, Decimal a, int b, Decimal modulo): pass
  Decimal power(Context self, int a, Decimal b, Decimal modulo): pass
  Decimal quantize(Context self, Decimal a, Decimal b): pass
  Decimal quantize(Context self, int a, int b): pass
  Decimal quantize(Context self, Decimal a, int b): pass
  Decimal quantize(Context self, int a, Decimal b): pass
  Decimal radix(Context self): pass
  Decimal remainder(Context self, Decimal a, Decimal b): pass
  Decimal remainder(Context self, int a, int b): pass
  Decimal remainder(Context self, Decimal a, int b): pass
  Decimal remainder(Context self, int a, Decimal b): pass
  Decimal remainder_near(Context self, Decimal a, Decimal b): pass
  Decimal remainder_near(Context self, int a, int b): pass
  Decimal remainder_near(Context self, Decimal a, int b): pass
  Decimal remainder_near(Context self, int a, Decimal b): pass
  Decimal rotate(Context self, Decimal a, Decimal b): pass
  Decimal rotate(Context self, int a, int b): pass
  Decimal rotate(Context self, Decimal a, int b): pass
  Decimal rotate(Context self, int a, Decimal b): pass
  bool same_quantum(Context self, Decimal a, Decimal b): pass
  bool same_quantum(Context self, int a, int b): pass
  bool same_quantum(Context self, Decimal a, int b): pass
  bool same_quantum(Context self, int a, Decimal b): pass
  Decimal scaleb(Context self, Decimal a, Decimal b): pass
  Decimal scaleb(Context self, int a, int b): pass
  Decimal scaleb(Context self, Decimal a, int b): pass
  Decimal scaleb(Context self, int a, Decimal b): pass
  Decimal shift(Context self, Decimal a, Decimal b): pass
  Decimal shift(Context self, int a, int b): pass
  Decimal shift(Context self, Decimal a, int b): pass
  Decimal shift(Context self, int a, Decimal b): pass
  Decimal sqrt(Context self, int a): pass
  Decimal sqrt(Context self, Decimal a): pass
  Decimal subtract(Context self, Decimal a, Decimal b): pass
  Decimal subtract(Context self, int a, int b): pass
  Decimal subtract(Context self, Decimal a, int b): pass
  Decimal subtract(Context self, int a, Decimal b): pass
  str to_eng_string(Context self, Decimal a): pass
  str to_eng_string(Context self, int a): pass
  Decimal to_integral(Context self, Decimal a): pass
  Decimal to_integral(Context self, int a): pass
  Decimal to_integral_exact(Context self, Decimal a): pass
  Decimal to_integral_exact(Context self, int a): pass
  Decimal to_integral_value(Context self, Decimal a): pass
  Decimal to_integral_value(Context self, int a): pass
  str to_sci_string(Context self, Decimal a): pass
  str to_sci_string(Context self, int a): pass
  dict __dict__
  list __weakref__

class DecimalException(builtins.ArithmeticError): # TODO test
  void handle(builtins.ArithmeticError self, Context context): pass
  void handle(builtins.ArithmeticError self, Context context, int sign): pass
  void handle(builtins.ArithmeticError self, Context context, int sign, any *args): pass
class DecimalTuple(builtins.tuple):
  tuple __getnewargs__(DecimalTuple self): pass
  str __repr__(DecimalTuple self): pass
  collections.OrderedDict _asdict(DecimalTuple self): pass
Context DefaultContext
class DivisionByZero(DecimalException, builtins.ZeroDivisionError): pass
class DivisionImpossible(InvalidOperation): pass
class DivisionUndefined(InvalidOperation, builtins.ZeroDivisionError): pass
Context ExtendedContext
class Inexact(DecimalException): pass
class InvalidContext(InvalidOperation): pass
class InvalidOperation(DecimalException): pass
class Overflow(Inexact, Rounded): pass
str ROUND_05UP
str ROUND_CEILING
str ROUND_DOWN
str ROUND_FLOOR
str ROUND_HALF_DOWN
str ROUND_HALF_EVEN
str OUND_HALF_UP
str ROUND_UP
class Rounded(DecimalException): pass
class Subnormal(DecimalException): pass
class Underflow(Inexact, Rounded, Subnormal): pass
class _ContextManager(builtins.object):
  typ __enter__<typ>(typ self): pass
  typ __exit__<typ>(typ self, any t, any v, any tb): pass
  void __init__<typ>(typ self, Context new_context): pass
Decimal _Infinity
class _Log10Memoize:
  int getdigits(_Log10Memoize self, int p): pass
  void __init__(_Log10Memoize self): pass # todo: is this necessary? also, can we use <t>(t self) rather than the classname? should we??
Decimal _NaN
Decimal _NegativeInfinity
Decimal _NegativeOne
Decimal _One
int _PyHASH_10INV
int _PyHASH_INF
int _PyHASH_MODULUS
int _PyHASH_NAN
tuple<Decimal, Decimal> _SignedInfinity
class _WorkRep: pass
Decimal _Zero
str __cached__
str __doc__
str __file__
#void __package__
str __version__
#_sre.SRE_Pattern.match _all_zeros
dict<DecimalException, DecimalException> _condition_map
tuple<Decimal, Decimal> _convert_for_comparison(Decimal self, object other, bool equality_op=False): pass
Decimal _convert_other(object other, bool raiseit=False, bool allow_float=False): pass
tuple<int,int> _dexp(int c, int e, int p): pass
int _div_nearest(int a, int b): pass
int _dlog(int c, int e, int p): pass
int _dlog10(int c, int e, int p): pass
tuple<int,int> _dpower(int xc, int xe, int yc, int ye, int p): pass
#_sre.SRE_Pattern.match _exact_half
str _format_align(str sign, str body, dict<str,type> spec): pass
str _format_number(bool is_negative, str intpart, str fracpart, int exp, dict<str,type> spec): pass
str _format_sign(bool is_negative, dict<str,type> spec): pass
list<int> _group_lengths(list<int> grouping): pass
int _iexp(int x, int M): pass
int _iexp(int x, int M, int L): pass
int _ilog(int x, int M): pass
int _ilog(int x, int M, int L): pass
str _insert_thousands_sep(str digits, dict<str,type> spec): pass
str _insert_thousands_sep(str digits, dict<str,type> spec, int min_width): pass
#any _locale
int _log10_digits(_Log10Memoize self, int p): pass
int _log10_lb(int c): pass
int _log10_lb(int c, dict<str,int> correction): pass
#any _math
#from collections import namedtuple as _namedtuple # TODO: missing in MyPy port of "collections"
int _nbits(int self): pass
tuple<Decimal, Decimal> _normalize(Decimal op1, Decimal op2): pass
tuple<Decimal, Decimal> _normalize(Decimal op1, Decimal op2, prec): pass
#any _numbers
def _parse_format_specifier(str format_spec): pass
def _parse_format_specifier(str format_spec, dict<str,type> _localeconv=None): pass
#_sre.SRE_Pattern _parse_format_specifier_regex
#_sre.SRE_Pattern.match _parser
Decimal remove_exponent(str d): pass
int _rshift_nearest(int x, int shift): pass
#any _signals
int _sqrt_nearest(int n, int a): pass
_ContextManager localcontext(): pass
_ContextManager localcontext(Context ctx): pass
Context getcontext(): pass
Context getcontext(any _local): pass # TODO _local=<_thread._local object>
void setcontext(Context context): pass
void setcontext(Context context, any _local): pass # TODO _thread._local


class Decimal:
  Decimal __abs__(Decimal self): pass
  Decimal __abs__(Decimal self, bool round): pass
  Decimal __abs__(Decimal self, bool round, Context context): pass
  Decimal __add__(Decimal self, Decimal other): pass
  Decimal __add__(Decimal self, int other): pass
  bool __bool__(Decimal self): pass
  int __ceil__(Decimal self): pass
  any __complex__(Decimal self): pass # TODO need MyPy support for complex
  any __copy__(Decimal self): pass
  any __deepcopy__(Decimal self): pass
  tuple<Decimal,Decimal> __divmod__(Decimal self, Decimal other): pass
  tuple<Decimal,Decimal> __divmod__(Decimal self, Decimal other, Context context): pass
  tuple<Decimal,Decimal> __divmod__(Decimal self, int other): pass
  tuple<Decimal,Decimal> __divmod__(Decimal self, int other, Context context): pass
  bool __eq__(Decimal self, any other): pass
  float __float__(Decimal self): pass
  int __floor__(Decimal self): pass
  Decimal __floordiv__(Decimal self, Decimal other): pass
  Decimal __floordiv__(Decimal self, Decimal other, context): pass
  Decimal __floordiv__(Decimal self, int other): pass
  Decimal __floordiv__(Decimal self, int other, context): pass
  str __format__(Decimal self, str specifier): pass
  str __format__(Decimal self, str specifier, Context context): pass
  str __format__(Decimal self, str specifier, Context context, dict<str,type> _localeconv): pass
  bool __ge__(Decimal self, Decimal other): pass
  bool __ge__(Decimal self, Decimal  other, Context context): pass
  bool __ge__(Decimal self, int other): pass
  bool __ge__(Decimal self, int other, Context context): pass
  bool __gt__(Decimal self, int other): pass
  bool __gt__(Decimal self, Decimal other): pass
  bool __gt__(Decimal self, int other, Context context): pass
  bool __gt__(Decimal self, Decimal other, Context context): pass
  int __hash__(Decimal self): pass
  int __int__(Decimal self): pass
  bool __le__(Decimal self, Decimal other): pass
  bool __le__(Decimal self, Decimal other, Context context): pass
  bool __le__(Decimal self, int other): pass
  bool __le__(Decimal self, int other, Context context): pass
  bool __lt__(Decimal self, Decimal other): pass
  bool __lt__(Decimal self, Decimal other, Context context): pass
  bool __lt__(Decimal self, int other): pass
  bool __lt__(Decimal self, int other, Context context): pass
  Decimal __mod__(Decimal self, Decimal other): pass
  Decimal __mod__(Decimal self, Decimal other, Context context): pass
  Decimal __mod__(Decimal self, int other): pass
  Decimal __mod__(Decimal self, int other, Context context): pass
  Decimal __mul__(Decimal self, int other): pass
  Decimal __mul__(Decimal self, int other, Context context): pass
  Decimal __mul__(Decimal self, Decimal other): pass
  Decimal __mul__(Decimal self, Decimal other, Context context): pass
  bool __ne__(Decimal self, Decimal other): pass
  bool __ne__(Decimal self, Decimal other, Context context): pass
  bool __ne__(Decimal self, int other): pass
  bool __ne__(Decimal self, int other, Context context): pass
  Decimal __neg__(Decimal self): pass
  Decimal __neg__(Decimal self, Context context): pass
  Decimal __pos__(Decimal self): pass
  Decimal __pos__(Decimal self, Context context): pass

  Decimal __pow__(Decimal self, int other): pass
  Decimal __pow__(Decimal self, Decimal other): pass

  Decimal __pow__(Decimal self, int other, int modulo): pass
  Decimal __pow__(Decimal self, Decimal other, int modulo): pass
  Decimal __pow__(Decimal self, int other, Decimal modulo): pass
  Decimal __pow__(Decimal self, Decimal other, Decimal modulo): pass

  Decimal __pow__(Decimal self, int other, int modulo, Context context): pass
  Decimal __pow__(Decimal self, Decimal other, int modulo, Context context): pass
  Decimal __pow__(Decimal self, int other, Decimal modulo, Context context): pass
  Decimal __pow__(Decimal self, Decimal other, Decimal modulo, Context context): pass
  Decimal __radd__(Decimal self, int other): pass
  Decimal __radd__(Decimal self, Decimal other): pass
  Decimal __radd__(Decimal self, int other, Context context): pass
  Decimal __radd__(Decimal self, Decimal other, Context context): pass
  tuple<Decimal,Decimal> __rdivmod__(Decimal self, Decimal other): pass
  tuple<Decimal,Decimal> __rdivmod__(Decimal self, Decimal other, Context context): pass
  tuple<Decimal,Decimal> __rdivmod__(Decimal self, int other): pass
  tuple<Decimal,Decimal> __rdivmod__(Decimal self, int other, Context context): pass
  tuple<Decimal,tuple> __reduce__(Decimal self): pass
  str __repr__(Decimal self): pass
  Decimal __rfloordiv__(Decimal self, int other): pass
  Decimal __rfloordiv__(Decimal self, int other, Context context): pass
  Decimal __rfloordiv__(Decimal self, Decimal other): pass
  Decimal __rfloordiv__(Decimal self, Decimal other, Context context): pass
  Decimal __rmod__(Decimal self, int other): pass
  Decimal __rmod__(Decimal self, int other, Context context): pass
  Decimal __rmod__(Decimal self, Decimal other): pass
  Decimal __rmod__(Decimal self, Decimal other, Context context): pass
  Decimal __rmul__(Decimal self, int other): pass
  Decimal __rmul__(Decimal self, int other, Context context): pass
  Decimal __rmul__(Decimal self, Decimal other): pass
  Decimal __rmul__(Decimal self, Decimal other, Context context): pass
  int __round__(Decimal self): pass
  int __round__(Decimal self, Decimal n): pass
  int __round__(Decimal self, int n): pass
  Decimal __rpow__(Decimal self, int other): pass
  Decimal __rpow__(Decimal self, int other, Context context): pass
  Decimal __rpow__(Decimal self, Decimal other): pass
  Decimal __rpow__(Decimal self, Decimal other, Context context): pass
  Decimal __rsub__(Decimal self, Decimal other): pass
  Decimal __rsub__(Decimal self, Decimal other, Context context): pass
  Decimal __rsub__(Decimal self, int other): pass
  Decimal __rsub__(Decimal self, int other, Context context): pass
  Decimal __rtruediv__(Decimal self, Decimal other): pass
  Decimal __rtruediv__(Decimal self, Decimal other, Context context): pass
  Decimal __rtruediv__(Decimal self, int other): pass
  Decimal __rtruediv__(Decimal self, int other, Context context): pass
  str __str__(Decimal self, bool eng=False, Context context=None): pass
  Decimal __sub__(Decimal self, int other, Context context=None): pass
  Decimal __sub__(Decimal self, Decimal other, Context context=None): pass  
  Decimal __truediv__(Decimal self, Decimal other, Context context=None): pass
  Decimal __truediv__(Decimal self, int other, Context context=None): pass
  int __trunc__(Decimal self): pass
  Decimal __floordiv__(Decimal self, Decimal other, Context context=None): pass
  Decimal __floordiv__(Decimal self, int other, Context context=None): pass
  void __init__(type cls, str value, Context context=None): pass
  void __init__(type cls, int value, Context context=None): pass
  void __init__(type cls, float value, Context context=None): pass
  int adjusted(Decimal self): pass
  DecimalTuple as_tuple(Decimal self): pass
  Decimal canonical(Decimal self): pass
  Decimal compare(Decimal self, Decimal other, Context context=None): pass
  Decimal compare(Decimal self, int other, Context context=None): pass
  Decimal compare_signal(Decimal self, Decimal other, Context context=None): pass
  Decimal compare_signal(Decimal self, int other, Context context=None): pass
  Decimal compare_total_mag(Decimal self, Decimal other): pass
  Decimal compare_total_mag(Decimal self, int other): pass
  Decimal conjugate(Decimal self): pass
  Decimal copy_abs(Decimal self): pass
  Decimal copy_negate(Decimal self): pass
  # copy_sign
  Decimal exp(Decimal self, Context context=None): pass
  Decimal from_float(Decimal self, float f): pass
  Decimal fma(Decimal self, Decimal other, Decimal third): pass
  Decimal fma(Decimal self, int other, int third): pass
  Decimal fma(Decimal self, Decimal other, int third): pass
  Decimal fma(Decimal self, int other, Decimal third): pass
  Decimal fma(Decimal self, Decimal other, Decimal third, Context context): pass
  Decimal fma(Decimal self, int other, int third, Context context): pass
  Decimal fma(Decimal self, Decimal other, int third, Context context): pass
  Decimal fma(Decimal self, int other, Decimal third, Context context): pass
  bool is_canonical(Decimal self): pass
  bool is_infinite(Decimal self): pass
  bool is_nan(Decimal self): pass
  bool is_normal(Decimal self): pass
  bool is_qnan(Decimal self): pass
  bool is_signed(Decimal self): pass
  bool is_snan(Decimal self): pass
  bool is_subnormal(Decimal self): pass
  bool is_zero(Decimal self): pass
  bool is_(Decimal a, Decimal b): pass
  Decimal ln(Decimal self, Context context=None): pass
  Decimal logb(Decimal self, Context context=None): pass
  Decimal log10(Decimal self, Context context=None): pass
  ## copy function definitions from Context
  

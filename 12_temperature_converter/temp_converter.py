"""Temperature Converter"""
def c_to_f(c): return c * 9/5 + 32
  def f_to_c(f): return (f - 32) * 5/9
    c = input("1.C->F 2.F->C: ")
t = float(input("Temp: "))
print(f"{c_to_f(t):.1f}F" if c=="1" else f"{f_to_c(t):.1f}C")

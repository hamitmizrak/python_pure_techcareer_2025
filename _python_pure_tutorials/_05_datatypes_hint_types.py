
# int, float, str, bool, list, tuple, set, dict  ==> hint types

# Eğer global bir değişken kullanıyorsanız altaki örneği yazabiliriz
value=44
value=44.44
value=True
value="Merhabalar"
print(value)

# Ancak veri karmaşıklığı yaşamamak adına bizler dataların güvenliğini sağlamak için type-hint kullanabiliriz
# Type Hint:
number: int=10
pi: float=3.14
value: str="Merhabalar"
is_login: bool=True
list_data :list[int]      = [1,2,3]
tuple_data:tuple[int,int] = (1,2)
dict_data:dict[str,int] = {"Merhabalar":44}
data: bytes=b"\x00\xff"
data_byte_arra:bytearray=bytearray(b"abc")
nothing:None | str =None # None olabilir veya str olabilir.
print(f"sayı {number} ==> type {type(number)}")

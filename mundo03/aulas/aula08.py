try:
  a = int(input("Numerador: "))
  b = int(input("Denominador: "))
  r = a / b
#except (ValueError, TypeError, ZeroDivisionError):
#  print("Problema com os tipos de dados.")
except KeyboardInterrupt:
  print("Dados não informados.")
except ValueError:
  print("Erro de valor.")
except TypeError:
  print("Erro de tipo.")
except ZeroDivisionError:
  print("Tá dividindo por zero burrão!")
except Exception as erro:
  print("Num funcionou naum em!")
  print(f"O erro foi {erro.__class__}")
  print(f"O erro foi {erro.__cause__}")
else: # opcional
  print(f"O resultado é {r:.1f}")
finally: # opcional, funciona sempre
  print("Tamo junto milkshake.")


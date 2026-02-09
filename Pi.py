from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP
import math

# True value of pi
true_pi = Decimal(str(math.pi))

# Decimal precisions
precisions = [20, 40, 60, 100]

# Sphere volume (r = 10 to match ~6283 scale)
def sphere_volume(pi_value):
    r = Decimal(10)
    return (Decimal(4) / Decimal(3)) * pi_value * (r ** 3)

# ===================== PART A =====================
print("=" * 55)
print("COMPARING TRUNCATED AND ROUNDED PI VALUES IN SPHERE VOLUME CALCULATION")
print("=" * 55)

# Baseline pi values
pi_trunc = true_pi.quantize(Decimal('1.0000'), rounding=ROUND_DOWN)    # 3.1415
pi_round = true_pi.quantize(Decimal('1.0000'), rounding=ROUND_HALF_UP) # 3.1416

# Volumes
vol_trunc = sphere_volume(pi_trunc)
vol_round = sphere_volume(pi_round)
vol_true = sphere_volume(true_pi)

print(f"\nTRUNCATED - 3.1415: {vol_trunc:.4f}")
print(f"REAL VOLUME      : {vol_true:.5f}")
print(f"ROUNDED - 3.1416: {vol_round:.4f}")

print(f"\nTHEIR DIFFERENCES:")
print(f"TRUNCATION ERROR: {abs(vol_true - vol_trunc):.5f}")
print(f"ROUNDING ERROR: {abs(vol_true - vol_round):.5f}")

# ===================== PART B =====================
print("\n" + "=" * 55)
print("COMPARING THE DIFFERENT PI VALUES AT VARIOUS PRECISIONS")
print("=" * 55)

for p in precisions:
    getcontext().prec = p

    vol_true_p = sphere_volume(true_pi)
    vol_trunc_p = sphere_volume(pi_trunc)
    vol_round_p = sphere_volume(pi_round)

    print(f"\n===CALCULATING AT {p} DECIMAL PLACES ===")
    print(f"Real Volume : {vol_true_p}")
    print(f"Truncated Volume: {vol_trunc_p}")
    print(f"Rounded Volume: {vol_round_p}")

    if vol_trunc_p == vol_round_p:
        print("RESULT: THE SAME.")
    else:
        print("RESULT: DIFFERENT.")

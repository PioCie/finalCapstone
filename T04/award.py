swimming_time = int(input("After how many minutes did you complete the swimming stage? "))
cycling_time = int(input("After how many minutes did you complete the cycling stage? "))
running_time = int(input("After how many minutes did you complete the running stage? "))

total_time = (swimming_time + cycling_time + running_time)

if total_time <= 100:
    print(f"Congratulations on completing the Triathlon, it took you {total_time} minutes. You receive an award: "
          f"Provincial Colours")
elif total_time == 101 or total_time <= 105:
    print(f"Congratulations on completing the Triathlon, it took you {total_time} minutes. You receive an award: "
          f"Provincial Half Colours")
elif total_time == 106 or total_time <= 110:
    print(f"Congratulations on completing the Triathlon, it took you {total_time} minutes. You receive an award: "
          f"Provincial Scroll")
else:
    print(f"Congratulations on completing the Triathlon, it took you {total_time} minutes. Unfortunately, you will "
          f"not receive any award")


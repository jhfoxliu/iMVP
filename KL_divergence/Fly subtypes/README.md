MotifComparison: http://bioinformatics.intec.ugent.be/MotifSuite/usemotifcomparison.php

### generate matrix file
python txt2pwm_all_v2.py -i Human_TypeI.txt Mouse_TypeI.txt XT_TypeI.txt XL_TypeI.txt ZF_TypeI.txt Fly_TypeI.txt Fly_sub1.txt Fly_sub2.txt Fly_sub3.txt > Fly_sub.mtrx

### calculate KL divergence
./MotifComparison -m Fly_sub.mtrx -b Fly_sub.mtrx > Fly_sub.out

#!/bin/bash
file=($(ls *))

for i in ${file[@]}
do
echo ${i}
if [ "${i}" != "GSTAr_out_reformat.sh" ]
then echo "awk '!/#/' ${i} > trim_${i}"
awk '!/^#/' ${i} > trim1_${i}
tail -n +2 trim1_${i} > trim2_${i}
cut -f1,2,3,4,5,8 trim2_${i} > out_${i}
rm -rf trim*
mv out_${i} ${i}
fi
done

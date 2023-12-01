import sys

sys.stdin = open("input.txt")
total = 0
while True:
    try:
        subtotal = (int(input()) // 3) - 2
        while subtotal > 0:
           total += subtotal
           subtotal = (subtotal // 3) - 2
    except EOFError:
        break


print(total)

    red_m = [N[i,j].r for i in 1:mr, j in 1:mc ]
	gre_m = [N[i,j].g for i in 1:mr, j in 1:mc ]
	blu_m = [N[i,j].b for i in 1:mr, j in 1:mc ]
	for i in 1:mr
		for j in 1:mc
			red_m_ij = [extend_mat(red_m, t, s) for t in i-lr:i+lr, s in j-lc:j+lc]
			gre_m_ij = [extend_mat(gre_m, t, s) for t in i-lr:i+lr, s in j-lc:j+lc]
			blu_m_ij = [extend_mat(blu_m, t, s) for t in i-lr:i+lr, s in j-lc:j+lc]
			k_red_ij = red_m_ij .* K
			k_gre_ij = gre_m_ij .* K
			k_blu_ij = blu_m_ij .* K
			new_m[i,j] = RGB(min(1,sum(k_red_ij)), min(1,sum(k_gre_ij)), min(1,sum(k_blu_ij)))
		end
	end



https://www.amazon.de/gp/product/B0050QB3EQ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
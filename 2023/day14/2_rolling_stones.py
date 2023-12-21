from copy import copy, deepcopy

grid = open('input.txt', 'r').read().split('\n')

n = len(grid)

def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='')
        print()
    print()


for l in range(n):
    grid[l] = list(grid[l])


def calculate_result(): 
    i = len(grid)
    result = 0
    for line in grid:
        result += i * line.count('O')
        i -= 1
    return result


def roll():
    for column in range(len(grid[0])): 
        for row in range(n):
            moved = False
            if grid[row][column] in '#.':
                continue
            if grid[row][column] == 'O':
                k = row - 1
                while  0 <= k < n - 1 and grid[k][column] == '.':
                    k -= 1
                    moved = True
                if moved:
                    grid[k + 1][column] = 'O'
                    grid[row][column] = '.'

    
def rotate():
    global grid
    n = len(grid)
    m = len(grid[0])
    rotated = [['']*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            rotated[i][j] = grid[n - 1 - j][i]

    grid = rotated

count = 1
#print_grid()
results = [calculate_result()]
last = deepcopy(grid)
for i in range(300):
    for _ in range(4):
        roll()
        rotate()
    result = calculate_result()
    # if result in results:
    #     idx = results.index(result)
    #     #print(result, idx, count, "period lenght", count - idx)
    # else:
    #     results.append(result)
    results.append(result)
    count += 1
    
# the values were found with heuristics, printing the repeated values
position = (1000000000  - 191) % 102 + 191 
print("Position and result", position, results[position])



3333


# 99690 2 32 period lenght 30
# 100238 46 51 period lenght 5
# 100234 48 53 period lenght 5
# 100198 44 55 period lenght 11
# 100010 37 61 period lenght 24
# 99704 68 74 period lenght 6
# 99253 89 98 period lenght 9
# 99522 103 111 period lenght 8
# 99507 76 117 period lenght 41
# 99454 12 119 period lenght 107
# 99415 98 120 period lenght 22
# 99384 110 122 period lenght 12
# 99253 89 128 period lenght 39
# 99234 22 130 period lenght 108
# 99241 116 132 period lenght 16
# 99484 29 142 period lenght 113
# 99558 106 147 period lenght 41
# 99488 101 152 period lenght 51
# 99411 124 154 period lenght 30
# 99356 82 158 period lenght 76
# 99241 116 162 period lenght 46
# 99237 88 163 period lenght 75
# 99250 118 164 period lenght 46
# 99237 88 165 period lenght 77
# 99237 88 166 period lenght 78
# 99534 133 179 period lenght 46
# 99554 131 181 period lenght 50
# 99570 105 182 period lenght 77
# 99427 148 188 period lenght 40
## Cycle begins at position 191
# 99371 83 191 period lenght 108
# 99344 84 192 period lenght 108
# 99316 85 193 period lenght 108
# 99307 86 194 period lenght 108
# 99263 87 195 period lenght 108
# 99237 88 196 period lenght 108
# 99253 89 197 period lenght 108
# 99238 90 198 period lenght 108
# 99233 91 199 period lenght 108
# 99253 89 200 period lenght 111
# 99254 92 201 period lenght 109
# 99274 93 202 period lenght 109
# 99318 94 203 period lenght 109
# 99339 95 204 period lenght 109
# 99365 96 205 period lenght 109
# 99406 97 206 period lenght 109
# 99415 98 207 period lenght 109
# 99436 99 208 period lenght 109
# 99473 100 209 period lenght 109
# 99488 101 210 period lenght 109
# 99497 102 211 period lenght 109
# 99522 103 212 period lenght 109
# 99522 103 213 period lenght 110
# 99533 104 214 period lenght 110
# 99570 105 215 period lenght 110
# 99558 106 216 period lenght 110
# 99544 107 217 period lenght 110
# 99546 108 218 period lenght 110
# 99507 76 219 period lenght 143
# 99472 109 220 period lenght 111
# 99454 12 221 period lenght 209
# 99415 98 222 period lenght 124
# 99384 110 223 period lenght 113
# 99384 110 224 period lenght 114
# 99359 111 225 period lenght 114
# 99340 112 226 period lenght 114
# 99332 113 227 period lenght 114
# 99295 114 228 period lenght 114
# 99259 115 229 period lenght 114
# 99253 89 230 period lenght 141
# 99241 116 231 period lenght 115
# 99234 22 232 period lenght 210
# 99249 117 233 period lenght 116
# 99241 116 234 period lenght 118
# 99250 118 235 period lenght 117
# 99290 119 236 period lenght 117
# 99306 120 237 period lenght 117
# 99335 121 238 period lenght 117
# 99381 122 239 period lenght 117
# 99394 123 240 period lenght 117
# 99411 124 241 period lenght 117
# 99452 125 242 period lenght 117
# 99461 126 243 period lenght 117
# 99484 29 244 period lenght 215
# 99513 127 245 period lenght 118
# 99510 128 246 period lenght 118
# 99518 129 247 period lenght 118
# 99549 130 248 period lenght 118
# 99558 106 249 period lenght 143
# 99554 131 250 period lenght 119
# 99560 132 251 period lenght 119
# 99534 133 252 period lenght 119
# 99503 134 253 period lenght 119
# 99488 101 254 period lenght 153
# 99442 135 255 period lenght 120
# 99411 124 256 period lenght 132
# 99400 136 257 period lenght 121
# 99372 137 258 period lenght 121
# 99355 138 259 period lenght 121
# 99356 82 260 period lenght 178
# 99320 139 261 period lenght 122
# 99291 140 262 period lenght 122
# 99275 141 263 period lenght 122
# 99241 116 264 period lenght 148
# 99237 88 265 period lenght 177
# 99250 118 266 period lenght 148
# 99237 88 267 period lenght 179
# 99237 88 268 period lenght 180
# 99266 142 269 period lenght 127
# 99278 143 270 period lenght 127
# 99302 144 271 period lenght 127
# 99351 145 272 period lenght 127
# 99369 146 273 period lenght 127
# 99390 147 274 period lenght 127
# 99427 148 275 period lenght 127
# 99440 149 276 period lenght 127
# 99457 150 277 period lenght 127
# 99500 151 278 period lenght 127
# 99501 152 279 period lenght 127
# 99506 153 280 period lenght 127
# 99534 133 281 period lenght 148
# 99537 154 282 period lenght 128
# 99554 131 283 period lenght 152
# 99570 105 284 period lenght 179
# 99548 155 285 period lenght 130
# 99530 156 286 period lenght 130
# 99519 157 287 period lenght 130
# 99476 158 288 period lenght 130
# 99438 159 289 period lenght 130
# 99427 148 290 period lenght 142
# 99388 160 291 period lenght 131
# 99368 161 292 period lenght 131
## Cycle ends at position 292 and has length 102
# 99371 83, 293 period lenght 210
# 99344 84, 294 period lenght 210
# 99316 85, 295 period lenght 210
# 99307 86, 296 period lenght 210
# 99263 87, 297 period lenght 210
# 99237 88, 298 period lenght 210
# 99253 89, 299 period lenght 210
# 99238 90, 300 period lenght 210
# 99233 91, 301 period lenght 210
# 99253 89, 302 period lenght 213
# 99254 92, 303 period lenght 211
# 99274 93, 304 period lenght 211
# 99318 94, 305 period lenght 211
# 99339 95, 306 period lenght 211
# 99365 96, 307 period lenght 211
# 99406 97, 308 period lenght 211
# 99415 98, 309 period lenght 211
# 99436 99, 310 period lenght 211
# 99473 100, 311 period lenght 211
# 99488 101, 312 period lenght 211
# 99497 102, 313 period lenght 211
# 99522 103, 314 period lenght 211
# 99522 103, 315 period lenght 212
# 99533 104, 316 period lenght 212
# 99570 105, 317 period lenght 212
# 99558 106, 318 period lenght 212
# 99544 107, 319 period lenght 212
# 99546 108, 320 period lenght 212
# 99507 76 ,321 period lenght 245
# 99472 109, 322 period lenght 213
# 99454 12 ,323 period lenght 311
# 99415 98 ,324 period lenght 226
# 99384 110, 325 period lenght 215
# 99384 110, 326 period lenght 216
# 99359 111, 327 period lenght 216
# 99340 112, 328 period lenght 216
# 99332 113, 329 period lenght 216
# 99295 114, 330 period lenght 216
# 99259 115, 331 period lenght 216
# 99253 89 ,332 period lenght 243
# 99241 116, 333 period lenght 217
# 99234 22 ,334 period lenght 312
# 99249 117, 335 period lenght 218
# 99241 116, 336 period lenght 220
# 99250 118, 337 period lenght 219
# 99290 119, 338 period lenght 219
# 99306 120, 339 period lenght 219
# 99335 121, 340 period lenght 219
# 99381 122, 341 period lenght 219
# 99394 123, 342 period lenght 219
# 99411 124, 343 period lenght 219
# 99452 125, 344 period lenght 219
# 99461 126, 345 period lenght 219
# 99484 29 ,346 period lenght 317
# 99513 127, 347 period lenght 220
# 99510 128, 348 period lenght 220
# 99518 129, 349 period lenght 220
# 99549 130, 350 period lenght 220
# 99558 106, 351 period lenght 245
# 99554 131, 352 period lenght 221
# 99560 132, 353 period lenght 221
# 99534 133, 354 period lenght 221
# 99503 134, 355 period lenght 221
# 99488 101, 356 period lenght 255
# 99442 135, 357 period lenght 222
# 99411 124, 358 period lenght 234
# 99400 136, 359 period lenght 223
# 99372 137, 360 period lenght 223
# 99355 138, 361 period lenght 223
# 99356 82 ,362 period lenght 280
# 99320 139, 363 period lenght 224
# 99291 140, 364 period lenght 224
# 99275 141, 365 period lenght 224
# 99241 116, 366 period lenght 250
# 99237 88 ,367 period lenght 279
# 99250 118, 368 period lenght 250
# 99237 88 ,369 period lenght 281
# 99237 88 ,370 period lenght 282
# 99266 142, 371 period lenght 229
# 99278 143, 372 period lenght 229
# 99302 144, 373 period lenght 229
# 99351 145, 374 period lenght 229
# 99369 146, 375 period lenght 229
# 99390 147, 376 period lenght 229
# 99427 148, 377 period lenght 229
# 99440 149, 378 period lenght 229
# 99457 150, 379 period lenght 229
# 99500 151, 380 period lenght 229
# 99501 152, 381 period lenght 229
# 99506 153, 382 period lenght 229
# 99534 133, 383 period lenght 250
# 99537 154, 384 period lenght 230
# 99554 131, 385 period lenght 254
# 99570 105, 386 period lenght 281
# 99548 155, 387 period lenght 232
# 99530 156, 388 period lenght 232
# 99519 157, 389 period lenght 232
# 99476 158, 390 period lenght 232
# 99438 159, 391 period lenght 232
# 99427 148, 392 period lenght 244
# 99388 160, 393 period lenght 233
# 99368 161, 394 period lenght 233


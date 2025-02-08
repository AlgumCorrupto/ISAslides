from manim import *
from manim_slides import Slide
import re
import random

class Scn(Slide):
    def construct(self):
        self.camera.background_color =  ManimColor.from_hex('#0d1117')
        title = Text("Instruction Set Architectures", weight=BOLD)
        subtitle = Text("Criado por Paulo Villaça")
        subtitle.next_to(title, DOWN)
        tt = VGroup(title, subtitle)
        tt.center()
        self.play(Write(tt))
        self.next_slide()
        self.fadeAll()
        self.do_intro()
        self.next_slide()
        self.fadeAll()
        self.parse_st("sample.st")
        self.next_slide()
        self.fadeAll()
        self.do_esolangs()
        self.next_slide()
        self.fadeAll()
        self.do_oisc()
        self.next_slide()
        self.fadeAll()
        self.parse_fj("sample.fj")
        self.next_slide()
        self.fadeAll()
        self.do_risc()
        self.next_slide()
        self.fadeAll()
        self.parse_bf("sample.bf")
        self.next_slide()
        self.fadeAll()
        self.do_cisc()
        self.next_slide()
        self.fadeAll()
        self.do_cpu()
        self.next_slide()
        self.fadeAll()
        self.do_pl()
        self.next_slide()
        self.fadeAll()

    def fadeAll(self): 
        self.play(*[FadeOut(mob)for mob in self.mobjects])

    def do_esolangs(self):
        title = Text("Esolangs")
        title.to_edge(UL)
        points = BulletedList(
            "São linguagens esotéricas. Usados em meios\\\\ didáticos.",
            "Possivel classifica-las usando ISAs.",
            "Vamos exemplificar OISC e RISC usando esolangs."
        )
        self.play(Write(title))
        self.play(Write(points))

    def do_cpu(self):
        title = Text("Sobre CPUs")
        title.to_edge(UL)
        self.play(Write(title))
       
        points = BulletedList(
            "RISC\\\\ Desvantagem: $-$ instruções. \\\\Vantagem: instruções executadas \\\\ mais rapidamente.",
            "CISC\\\\ Desvantagem: instruções de propósito\\\\ geral demoram mais. \\\\Vantagem: $+$ instruções."
        )

        self.play(Write(points))
        self.wait(3)

    def do_cisc(self):
        title = Text("CISC")
        title.to_edge(UL)
        self.play(Write(title))
       
        points = BulletedList(
            "São os conjuntos de instruções\\\\ que contém vários subconjuntos",
            "Como no caso do\\\\ amd64, 8080, x86",
            "Não existe linguagem esotérca CISC.\\\\O mais próximo são linguagens\\\\multi-paradigma.",
        )
        self.play(Write(points))
        self.wait(3)

    def do_risc(self):
        title = Text("RISC")
        title.to_edge(UL)
        self.play(Write(title))
       
        points = BulletedList(
            "Há apenas instruções de propósito geral, que são as de: \\\\ manipulação de memória, controle e aritmética.",
            "ARM, MIPS são exemplos de RISC",
            "Linguagem exemplificada chama-se Brainfuck."
        )
        self.play(Write(points))
        self.next_slide()
        self.fadeAll()

        title = Text("Brainfuck")
        title.to_edge(UL)
        self.play(Write(title))

        points = BulletedList(
            "Uma interpretação de uma Máquina de Turing.",
            "Na maioria das implementações\\\\há um número de 30.000 células de memória.",
            "Cada célula de memória tem largura de 8-bits,\\\\seu tipo é unsigned integer\\\\(0 - 255).",
            "Há 2 ponteiros: memory pointer, program pointer."
        )
        self.play(Write(points))

        self.next_slide()
        self.play(FadeOut(points))
        title2 = Text("Brainfuck - Operadores:")
        title2.to_edge(UL)
        self.play(ReplacementTransform(title, title2))
        points = BulletedList(
            "$+$ $-$: incrementa/decrementa o valor apontado.",
            "$>$ $<$: incrementa/decrementa o memory pointer.",
            "$[$ $]$: instruções de looping.\\\\", 
            "$[$: vai para o $]$ correspondente\\\\se o valor apontado for 0.\\\\", 
            "$]$: vai para o $[$ correspondene\\\\se o valor apontado for diferente de 0."
        )
        self.play(Write(points))

    def do_oisc(self):
        title = Text("OISC")
        title.to_edge(UL)
        self.play(Write(title))
       
        points = BulletedList(
            "Há apenas uma instrução em todo\\\\ seu conjunto de instruções.",
            "Uma linguagem OISC chama-se FlipJump.",
        )
        self.play(Write(points))
        self.next_slide()
        self.fadeAll()
        title = Text("FlipJump")
        title.to_edge(UL)
        self.play(Write(title))

        points = BulletedList(
            "Versão mostrada é apenas\\\\uma simplificação.",
            "Versão original é turing complete.",
            "Memória composta por\\\\células de largura 1 bit.",
            "3 ponteiros, memory pointer, \\\\offset relativo ao memory pointer, program pointer."
        )
        self.play(Write(points))
        self.next_slide()
        self.play(FadeOut(points))
        title2 = Text("FlipJump - Instrução")
        title2.to_edge(UL)
        subtitle = Text("A instrução equivale a essa expressão em C:", font_size=21)
        

        subtitle.next_to(title, DOWN)
        subtitle.align_to(title, LEFT)
        self.play(ReplacementTransform(title, title2), Write(subtitle))
        code = Code(
            "fj.c",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color="WHITE",
            background="window",
            insert_line_no=False,
            style=Code.styles_list[15],
            language="c"
        )
        self.play(FadeIn(code))

    def do_intro(self):
        title = Text("Índice")
        title.to_edge(UL)
        self.play(Write(title))
       
        points = BulletedList(
            "Definição.",
            "Contextualizando usando esolangs.",
            "Um pouco sobre arquiteturas modernas.",
            "Finalizando com pipelines."
        )
        self.play(Write(points))
        self.next_slide()
        self.play(FadeOut(points))

        title2 = Text("Instruction Set Architectures")
        title2.to_edge(UL)
        self.play(ReplacementTransform(title, title2))

        points2 = BulletedList(
            "Instruction Set -- Conjunto de possíveis\\\\ operações em um contexto.",
            "ISAs -- formas de classificar esse\\\\ conjunto de instruções.",
            "As mais conhecidas são RISC \& CISC,\\\\ apesar de existirem outras."
        )

        self.play(Write(points2))
        self.next_slide()

    def parse_st(self, codefile: str):
        title = Text("Exemplo sobre conjunto de instruções")
        title.to_corner(UL)
        opcodes = BulletedList(
            "colocar -- adiciona item da pilha.",
            "tirar -- remove item da pilha.",
            "trocar -- últimos elementos de posição.",
            buff=MED_SMALL_BUFF
        )
        opcodes.scale(0.8)
        opcodes.next_to(title, DOWN)
        opcodes.align_to(title, LEFT)
        codecontent = Code(
            codefile,
            tab_width=4,
            background="window",
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=False,
            style=Code.styles_list[15],
            language="brainfuck"
        )

        codecontent.to_corner(DL)
        colorVals = [
            BLUE_A,
            TEAL_A,
            GREEN_A,
            YELLOW_A,
            GOLD_A,
            RED_A,
            MAROON_A,
            PURPLE_A
        ]
      
        random.seed(69420)
        stack = []
        programPointer = Arrow(RIGHT, LEFT, max_stroke_width_to_length_ratio=0)
        programPointer.next_to(codecontent.code[0], RIGHT)

        A = [3,0.5,0]
        B = [3,-3.5, 0]
        C = [6,-3.5,0]
        D = [6,0.5,0]

        corners = [A, B, C, D]
        bucket = Group ()

        for i in range(3):
            line = Line(
            start=corners[i],
            end=corners[i+1],
            )
            bucket.add(line)
        self.play(FadeIn(title, opcodes, codecontent, bucket, programPointer))

        code = open(codefile).readlines()
        self.next_slide()
        for i in range(0, len(code)):
            self.play(programPointer.animate.next_to(codecontent.code[i], RIGHT))
            match code[i].strip():
                case "colocar":
                    color = colorVals[random.randint(0, len(colorVals)-1)]
                    stack.append(
                       Rectangle(color, width=3, height=1) 
                    )
                    stack[-1].set_fill(color, opacity=1.0)
                    stack[-1].next_to(bucket[1], UP, buff=0)
                    stack[-1].shift(UP * (len(stack) - 1))
                    stack[-1].shift(UP * 3)
                    self.play(FadeIn(stack[-1]), stack[-1].animate.next_to(bucket[1], UP, buff=0).shift(UP * (len(stack) - 1)))
                case "tirar":
                    self.play(
                        stack[-1].animate.shift(UP * 3)
                    )
                    self.play(
                        FadeOut(stack[-1])
                    )
                    stack.pop()
                case "trocar":
                    st1 = stack[-1]
                    st2 = stack[-2]
                    temp = stack[-1].copy()
                    stack[-1] = stack[-2].copy()
                    stack[-2] = temp
                    self.remove(st1, st2)
                    self.play(
                        stack[-1].animate.shift(UP),
                        stack[-2].animate.shift(DOWN)
                    )



    def parse_bf(self, codefile: str):
        code =  open(codefile).read()
        codeunfiltered = "".join(filter(lambda c: c != '@', code))
        # memory section
        memsection = Rectangle(WHITE, height=8, width=4.0)
        memsection.to_edge(UR, 0)
        memlabel = Text("Memory", font="Monospace")
        memlabel.next_to(memsection, UP)
        memlabel.shift(DOWN * 1.1)
 
        memgrid = Rectangle(WHITE, height=1, width=3.0)
        memidrect = Rectangle(WHITE, height=1, width=1)
        memidrect.next_to(memgrid, LEFT, buff=0)
        memvalue =  DecimalNumber(0, 0, color=WHITE)
        memvalue.move_to(memgrid.get_center())
        memidlabel = DecimalNumber(0, 0, color=WHITE)
        memidlabel.move_to(memidrect.get_center())
        memid = VGroup(memidrect, memidlabel)
        memcell = [VGroup(memgrid, memid, memvalue)]

        memcell[0].next_to(memlabel, DOWN * 0.6)
        for i in range(1, 7):
            memcell.append(memcell[0].copy())
            memcell[i][1][1].set_value(i)
            memcell[i].next_to(memcell[i-1], DOWN, buff=0)
        # placeholder gyatt
        #mem2 = memcell.copy()
        #mem2.next_to(memcell, DOWN, buff=0)
        #mem3 = memcell.copy()
        #mem3.next_to(mem2, DOWN, buff=0)
        #mem4 = memcell.copy()
        #mem4.next_to(mem3, DOWN, buff=0)
        #mem5 = memcell.copy()
        #mem5.next_to(mem4, DOWN, buff=0)
        #mem6 = memcell.copy()
        #mem6.next_to(mem5, DOWN, buff=0)
        #mem7 = memcell.copy()
        #mem7.next_to(mem6, DOWN, buff=0)
        
        ram = [0,0,0,0,0,0,0]


        # code section
        coderect = Rectangle(WHITE, height=8, width=10.2)
        coderect.to_edge(UL, buff=0)
        codelabel = Text("Code:", color=WHITE, font="Monospace")
        codelabel.to_edge(UL, buff=0.2)
        codecontent = Code(
            codefile,
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=False,
            style=Code.styles_list[15],
            language="brainfuck",
        )
        code = open(codefile).readlines()
        codecontent.scale_to_fit_width(8)
        codecontent.move_to(coderect.get_center())
        codecontent.shift(DOWN * 0.3)


        # do the actual parsing ##########################
        linepointer = 0
        columnpointer = 0
        memorypointer = 0
        loopstack = []
        currLoop = -1
        ignoringId = -1
        isEOF = lambda : (columnpointer + 1) == len(codecontent.code) and (linepointer + 1) == len(codecontent.code[-1])
        currmemory = lambda : memcell[memorypointer][2]
        programArrow = Arrow(max_stroke_width_to_length_ratio=0, start=UP, end=DOWN)
        programArrow.next_to(codecontent.code[0][0], UP)
        memoryArrow = Arrow(max_stroke_width_to_length_ratio=0, start=LEFT, end=RIGHT)
        memoryArrow.next_to(memcell[0], LEFT)
        self.play(FadeIn(
            memsection, memlabel, *memcell,
            codelabel, coderect, codecontent
        ))
        self.play(FadeIn(programArrow, memoryArrow))
        self.wait(2)
        self.next_slide()
        while not isEOF():
            if code[columnpointer][linepointer] == '\n':
                columnpointer = columnpointer + 1
                linepointer = 0
            else:
                if code[columnpointer][linepointer] == '[':
                    if ram[memorypointer] == 0 and ignoringId == -1:
                        ignoringId = len(loopstack)
                    else: 
                        loopstack.append((columnpointer, linepointer))
                    currLoop += 1

                elif code[columnpointer][linepointer] == ']':
                    if ram[memorypointer] == 0:
                        if ignoringId == currLoop:
                            ignoringId = -1
                            self.play(programArrow.animate.next_to(codecontent.code[columnpointer][linepointer], UP))
                        currLoop -= 1
                    else:
                        columnpointer, linepointer = loopstack[currLoop]
                        self.play(programArrow.animate.next_to(codecontent.code[columnpointer][linepointer], UP))

                if ignoringId == -1:
                    if code[columnpointer][linepointer] == '-':
                        ram[memorypointer] = (ram[memorypointer] - 1) % 256
                        self.play(currmemory().animate.set_value(ram[memorypointer]))
                    elif code[columnpointer][linepointer] == '+':
                        ram[memorypointer] = (ram[memorypointer] + 1) % 256
                        self.play(currmemory().animate.set_value(ram[memorypointer]))
                    elif code[columnpointer][linepointer] == '>':
                        memorypointer += 1
                        self.play(memoryArrow.animate.next_to(memcell[memorypointer], LEFT))
                    elif code[columnpointer][linepointer] == '<':
                        memorypointer -= 1
                        self.play(memoryArrow.animate.next_to(memcell[memorypointer], LEFT))
                linepointer += 1
                if ignoringId == -1:
                    self.play(programArrow.animate.next_to(codecontent.code[columnpointer][linepointer], UP))
        

    def parse_fj(self, codefile: str):
        title = Text("FlipJump")
        title.to_edge(UL)
        self.play(Write(title))
        self.wait()
        # prologue ##############################
        # create code snippet
        codegui = Code(
            codefile,
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color="WHITE",
            background="window",
            insert_line_no=False,
            style=Code.styles_list[15],
            language="cpp"
        )
        codegui.to_edge(UP)
        codegui.shift(DOWN)
        self.play(FadeIn(codegui))

        programPointer = Arrow(start=LEFT, end=RIGHT, color=BLUE)
        programPointer.next_to(codegui.code[0], LEFT)
        code = open(codefile).readlines()
        memsize = int(re.findall("memsize ([0-9]+)", code[0])[0])
        # create memcells template
        memcellrect = Rectangle(WHITE, height=0.7, width=0.7)
        memcellnumber = DecimalNumber(0, num_decimal_places=0, unit_buff_per_font_unit=0.003)
        memcellnumber.move_to(memcellrect.get_center())
        memcell = VGroup(memcellnumber, memcellrect)
        ramtemp = []
        for i in range(memsize):
            buffcell = memcell.copy()
            if i != 0:
                buffcell.next_to(ramtemp[i-1], buff=0)
            ramtemp.append(buffcell)
        ramdisplay = VGroup(*ramtemp)
        ramdisplay.shift(-ramdisplay.get_center())
        ramdisplay.to_edge(DOWN)
        self.play(FadeIn(programPointer, ramdisplay))
        self.wait()
        mempointer = 0
        currMem = ramdisplay[mempointer]
        pointerArrow = Arrow(start=UP, end=DOWN, color=RED)
        pointerArrow.next_to(currMem, UP)
        currMemRect = memcellrect.copy()
        currMemRect.move_to(currMem.get_center())
        currMemRect.set_color(GREEN_B)

        self.play(FadeIn(pointerArrow, currMemRect))
        # Do the actual eval of the instructions ############################
        self.next_slide()
        for i in range(1, len(code)):
            if code[i] == "\n":
                continue
            flip, jump = re.findall(r"(\-*[0-9]+) +(\-*[0-9]+)", code[i])[0]
            currMem = ramdisplay[mempointer + int(flip)]
            self.play(
                pointerArrow.animate.next_to(ramdisplay[mempointer], UP)
            )
            self.play(
                programPointer.animate.next_to(codegui.code[i], LEFT),
            )
            direction = 1 if currMem.get_edge_center(UP)[0] - pointerArrow.get_tip().get_center()[0] >= 0 else -1
            offset = CurvedArrow(
                start_point=pointerArrow.get_tip().get_center(),
                end_point=currMem.get_edge_center(UP),
                color=GREEN,
                angle=-PI/4 * direction
            )
            self.play(
                Write(offset),
                currMemRect.animate.move_to(currMem[1].get_center())
            )
            self.play(
                currMem[0].animate.set_value(not currMem[0].get_value())
            )
            self.wait()
            self.play(Unwrite(offset))
            mempointer = int(jump)
        self.play(
            pointerArrow.animate.next_to(ramdisplay[mempointer], UP)
        )
        self.wait()
    
    def do_pl(self):
        title = Text("Sem pipeline")
        title.to_edge(UL)
        self.add(title)
        ins0 = self.makeInstrLine("INS_0")
        ins1 = self.makeInstrLine("INS_1") 
        ins2 = self.makeInstrLine("INS_2") 
        ins0.center()
        ins0.shift(UP * 1.5)
        ins1.next_to(ins0, DOWN*3)
        ins2.next_to(ins1, DOWN*3)
        insv = VGroup(ins0, ins1, ins2)
        insv.center()
        insv.shift(RIGHT * 0.5)
        self.play(FadeIn(insv))

        microIns0 = Rectangle(RED_B, height=0.8, width=0.8)
        microIns0.set_fill(RED_B, opacity=1.0)

        microIns1 = Rectangle(GREEN_B, height=0.8, width=0.8)
        microIns1.set_fill(GREEN_B, opacity=1.0)

        microIns2 = Rectangle(BLUE_B, height=0.8, width=0.8)
        microIns2.set_fill(BLUE_B, opacity=1.0)
        self.next_slide()

        i0m0 = microIns0.copy()
        self.positionMicro(i0m0, insv[0][1], 0)
        i0m1 = microIns1.copy()
        self.positionMicro(i0m1, insv[0][1], 1)
        i0m2 = microIns2.copy()
        self.positionMicro(i0m2, insv[0][1], 2)
        self.play(FadeIn(i0m0, i0m1, i0m2))

        i1m0 = microIns0.copy()
        self.positionMicro(i1m0, insv[1][1], 3)
        i1m1 = microIns1.copy()
        self.positionMicro(i1m1, insv[1][1], 4)
        i1m2 = microIns2.copy()
        self.positionMicro(i1m2, insv[1][1], 5)
        self.play(FadeIn(i1m0, i1m1, i1m2))

        i2m0 = microIns0.copy()
        self.positionMicro(i2m0, insv[2][1], 6)
        i2m1 = microIns1.copy()
        self.positionMicro(i2m1, insv[2][1], 7)
        i2m2 = microIns2.copy()
        self.positionMicro(i2m2, insv[2][1], 8)
        self.play(FadeIn(i2m0, i2m1, i2m2))

        self.next_slide()
        # FASE 2
        title2 = Text("Com pipeline")
        title2.to_edge(UL)
        self.play(ReplacementTransform(title, title2))

        i20m0 = microIns0.copy()
        self.positionMicro(i20m0, insv[0][1], 0)
        i20m1 = microIns1.copy()
        self.positionMicro(i20m1, insv[0][1], 1)
        i20m2 = microIns2.copy()
        self.positionMicro(i20m2, insv[0][1], 2)

        i21m0 = microIns0.copy()
        self.positionMicro(i21m0, insv[1][1], 1)
        i21m1 = microIns1.copy()
        self.positionMicro(i21m1, insv[1][1], 2)
        i21m2 = microIns2.copy()
        self.positionMicro(i21m2, insv[1][1], 3)
 

        i22m0 = microIns0.copy()
        self.positionMicro(i22m0, insv[2][1], 2)
        i22m1 = microIns1.copy()
        self.positionMicro(i22m1, insv[2][1], 3)
        i22m2 = microIns2.copy()
        self.positionMicro(i22m2, insv[2][1], 4)
        self.play(
            ReplacementTransform(i0m0, i20m0),
            ReplacementTransform(i0m1, i20m1),
            ReplacementTransform(i0m2, i20m2),

            ReplacementTransform(i1m0, i21m0),
            ReplacementTransform(i1m1, i21m1),
            ReplacementTransform(i1m2, i21m2),

            ReplacementTransform(i2m0, i22m0),
            ReplacementTransform(i2m1, i22m1),
            ReplacementTransform(i2m2, i22m2),
        )
        self.next_slide()

        # FASE 3
        ins0 = Text("MOV r0, 1", font="Monospace", font_size=32)
        ins1 = Text("ADD 1, r0", font="Monospace", font_size=32)
        ins2 = Text("ADD r1, 5", font="Monospace", font_size=32)

        ins0.move_to(insv[0][0].get_center())
        ins0.shift(LEFT * 0.5)
        ins1.move_to(insv[1][0].get_center())
        ins1.shift(LEFT * 0.5)
        ins2.move_to(insv[2][0].get_center())
        ins2.shift(LEFT * 0.5)

        self.play(
            ReplacementTransform(insv[0][0], ins0),
            ReplacementTransform(insv[1][0], ins1),
            ReplacementTransform(insv[2][0], ins2),
        )

        i0m0 = microIns0.copy()
        self.positionMicro(i0m0, insv[0][1], 0)
        i0m1 = microIns1.copy()
        self.positionMicro(i0m1, insv[0][1], 1)
        i0m2 = microIns2.copy()
        self.positionMicro(i0m2, insv[0][1], 2)

        i1m0 = microIns0.copy()
        self.positionMicro(i1m0, insv[1][1], 3)
        i1m1 = microIns1.copy()
        self.positionMicro(i1m1, insv[1][1], 4)
        i1m2 = microIns2.copy()
        self.positionMicro(i1m2, insv[1][1], 5)

        i2m0 = microIns0.copy()
        self.positionMicro(i2m0, insv[2][1], 4)
        i2m1 = microIns1.copy()
        self.positionMicro(i2m1, insv[2][1], 5)
        i2m2 = microIns2.copy()
        self.positionMicro(i2m2, insv[2][1], 6)

        self.play(
            ReplacementTransform(i20m0, i0m0),
            ReplacementTransform(i20m1, i0m1),
            ReplacementTransform(i20m2, i0m2),

            ReplacementTransform(i21m0, i1m0),
            ReplacementTransform(i21m1, i1m1),
            ReplacementTransform(i21m2, i1m2),

            ReplacementTransform(i22m0, i2m0),
            ReplacementTransform(i22m1, i2m1),
            ReplacementTransform(i22m2, i2m2),
        )
        self.next_slide()

    def positionMicro(self, rect, place, offset):
        rect.move_to(place.get_center())
        rect.align_to(place, LEFT)
        rect.shift(RIGHT)
        rect.shift((RIGHT * 1.1) * offset)

        return rect


    def makeInstrLine(self, name: str):
        label = Text(name, font="Monospace", font_size=32)
        line = Line(LEFT, RIGHT * 10)

        label.next_to(line, LEFT)

        return VGroup(label, line)

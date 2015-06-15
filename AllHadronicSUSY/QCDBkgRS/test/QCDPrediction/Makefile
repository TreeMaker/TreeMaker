C=g++
LD=g++

ROOTCFLAGS=$(shell root-config --cflags)
ROOTLIBS=$(shell root-config --libs)

CFLAGS =
LFLAGS =

RCXX=$(CFLAGS) $(ROOTCFLAGS)
RLXX=$(LFLAGS) $(ROOTLIBS)

SRC1= Prediction.o

SRC2= Prediction_WithUncertainties.o

%.o: %.C %.h
		$(C) $(RCXX) -c $<

all: GetPrediction GetPrediction_WithUncertainties

GetPrediction.o: GetPrediction.C
		$(C) $(RCXX) -c $<

GetPrediction: $(SRC1) GetPrediction.o
		$(LD) $(SRC1) GetPrediction.o $(RLXX) -o GetPrediction.x
		@echo '-> GetPrediction.x created!'

GetPrediction_WithUncertainties.o: GetPrediction_WithUncertainties.C
		$(C) $(RCXX) -c $<

GetPrediction_WithUncertainties: $(SRC2) GetPrediction_WithUncertainties.o
		$(LD) $(SRC2) GetPrediction_WithUncertainties.o $(RLXX) -o GetPrediction_WithUncertainties.x
		@echo '-> GetPrediction_WithUncertainties.x created!'

clean:
		@rm -f *~
		@rm -f *.o 
		@rm -f *.x

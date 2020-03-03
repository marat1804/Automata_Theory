# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : version2.sm

from SMC import statemap


class AppClassState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def At(self, fsm):
        self.Default(fsm)

    def Colom(self, fsm):
        self.Default(fsm)

    def Digit(self, fsm, letter):
        self.Default(fsm)

    def Dot(self, fsm):
        self.Default(fsm)

    def EOS(self, fsm):
        self.Default(fsm)

    def Eq(self, fsm):
        self.Default(fsm)

    def Letter(self, fsm, letter):
        self.Default(fsm)

    def MailTo(self, fsm):
        self.Default(fsm)

    def Question(self, fsm):
        self.Default(fsm)

    def Unknown(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class Map1_Default(AppClassState):

    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Digit(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Colom(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def At(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Dot(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Eq(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Unknown(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Question(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def MailTo(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.ClearSMC()
        finally:
            fsm.setState(Map1.MailTo)
            fsm.getState().Entry(fsm)


class Map1_MailTo(Map1_Default):

    def Colom(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.checkMail() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.counterZero()
            finally:
                fsm.setState(Map1.NameTo)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.Colom(self, fsm)
        
    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        if ctxt.lenMailTo() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.Memorise(letter)
                ctxt.counterInc()
            finally:
                fsm.setState(endState)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(Map1.Error)
                fsm.getState().Entry(fsm)


class Map1_NameTo(Map1_Default):

    def At(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.nonZero() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.remName()
                ctxt.counterZero()
            finally:
                fsm.setState(Map1.ServerName)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.At(self, fsm)
        
    def Digit(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Memorise(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Memorise(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


class Map1_ServerName(Map1_Default):

    def Digit(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.ServerName)
            fsm.getState().Entry(fsm)


    def Dot(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.nonZero() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.counterZero()
                ctxt.clearMem()
            finally:
                fsm.setState(Map1.Zone)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.Dot(self, fsm)
        
    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.ServerName)
            fsm.getState().Entry(fsm)


class Map1_Zone(Map1_Default):

    def Digit(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.nonZero() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
            finally:
                fsm.setState(Map1.OK)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.EOS(self, fsm)
        
    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.Zone)
            fsm.getState().Entry(fsm)


    def Question(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.nonZero() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.counterZero()
                ctxt.clearMem()
            finally:
                fsm.setState(Map1.Subject)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.Question(self, fsm)
        
class Map1_Subject(Map1_Default):

    def Eq(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.checkSubject() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.counterZero()
                ctxt.clearMem()
            finally:
                fsm.setState(Map1.Text)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.Eq(self, fsm)
        
    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Memorise(letter)
        finally:
            fsm.setState(Map1.Subject)
            fsm.getState().Entry(fsm)


class Map1_Text(Map1_Default):

    def Digit(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.Text)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.lenText() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
            finally:
                fsm.setState(Map1.OK)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.EOS(self, fsm)
        
    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.Text)
            fsm.getState().Entry(fsm)


class Map1_OK(Map1_Default):
    pass

class Map1_Error(Map1_Default):
    pass

class Map1(object):

    MailTo = Map1_MailTo('Map1.MailTo', 0)
    NameTo = Map1_NameTo('Map1.NameTo', 1)
    ServerName = Map1_ServerName('Map1.ServerName', 2)
    Zone = Map1_Zone('Map1.Zone', 3)
    Subject = Map1_Subject('Map1.Subject', 4)
    Text = Map1_Text('Map1.Text', 5)
    OK = Map1_OK('Map1.OK', 6)
    Error = Map1_Error('Map1.Error', 7)
    Default = Map1_Default('Map1.Default', -1)

class AppClass_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, Map1.MailTo)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:

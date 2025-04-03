program TrayNotes;

uses
  Forms,
  NotesMain in 'NotesMain.pas' {FormMain};

{$R *.res}

begin
  Application.Initialize;
  Application.Title := 'Tray Notes';
  Application.CreateForm(TFormMain, FormMain);
  Application.Run;
end.
